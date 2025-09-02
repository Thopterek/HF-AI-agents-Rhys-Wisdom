# ------------------
# More complex agent
# depending on the following
# %pip install langgraph langchain_openai langchain_core
# the system should implement:
# 1.Process images document
# 2. Extract text using vision models (VLM)
# 3. Perfom calculations when needed (tools)
# 4. Analyze content and provide summary
# 5. Execute specific instructions depending on doc
# -------------------------------------------------
import base64
from typing import List, TypedDict, Annotated, Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.graph import START, StateGraph
from langgraph.prebuild import ToolNode, tools_condition
from IPython.display import Image, display

# ----------------------
# Defining Agent's State
# adding operators in the state:
# defining how they should interact
# (eg. of usage add_messages)
# ---------------------------
class AgentState(TypedDict):
    # Provided document
    input_file: Optional[str] # path to it
    messages: Annotated[list[AnyMessage], add_messages]

# ----------------
# Tool Preparation
# ----------------
vision_llm = ChatOpenAI(model="gpt-4o")

def extract_text(img_path: str) -> str:
    """
    Extract text from an image file using a multimodal model.

    This tool allows me to annalyze content of documents and other froms of images.
    """
    all_text = ""
    try:
        # Read image and encode as base64
        with open(img_path, "rb") as image_file:
            image_bytes = image_file.read()
        image_base64 = base64.b64encode(image_bytes).decode("utf-8")
        # Preparing the prompt to include the base64 image data
        message = [
                HumanMessage(
                    content=[
                        {
                            "type": "text",
                            "text": (
                                "Extract all the text from this image."
                                "Return only the extracted text, no explanations"
                                )
                            }
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_base64}"
                                }
                            }
                        ]
                    )
                ]
        # calling the vision model
        response = vision_llm.invoke(message)
        # appending the extracted text
        all_text += response.content + "\n\n"
        return all_text.strip()
    except Exception as e:
        # Error handling
        error_msg = f"Error while extracting text: {str(e)}"
        print(error_msg)
        return ""

def divide(a: int, b: int) -> float:
    """
    Divide a and b, a tool to handle division calculations
    """
    return a / b

# equiping the agent with tools
tools = [
        divide,
        extract_text
        ]

model = ChatOpenAI(model="gpt-4o")
llm_with_tools = model.bind_tools(tools, parallel_tool_calls=False)

# -----------------------------------
# Creation of individual steps: Nodes
# -----------------------------------
def assistant(state: AgentState):
    # System message
    textual_description_of_tool="""
    extract_text(img_path) -> str:
        Extract text from an image file using multimodal model.
        Args:
            img_path: A local image file path (strings).
        Returns:
            A single string containing the concatenated text extracted from each image
    divide(a: int, b: int) -> float:
        Divide a and b
    """
    image=state["input_file"]
    sys_msg = SystemMessage(content=f"""
    You are a helpful butler named Alfred that serves the user.
    You can analyse documents and run computations with provided tools:
    {textual_description_of_tool}
    You also have access to some optional images.
    Currently loaded one is: {image}
    """)
    return {
            "messages": [llm_with_tools.invoke([sys_msg] + state["messages"])],
            "input_file": state["input_file"]
            }

# -----------------------
# Using the ReAct Pattern
# 1. Reason about document and request
# 2. Act by using the tools
# 3. Observe the results
# 4. Repeat as necessary until fully done
# ---------------------------------------
builder = StateGraph(AgentState) # graphing out
# defining the nodes
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
# defining the edges
builder.add_edge(START, "assistant")
builder.add_conditional_edges(
        "assistant",
        # if the latest msg requiers tool route to it
        tools_condition
        )
builder.add_edge("tools", "assistant")
react_graph = builder.compile()
# Show the butler's thought process
display(Image(react_graph.get_graph(xray=True).draw_mermaid_png()))

# ----------------
# Butler in Action
# ----------------
messages = [HumanMessage(content="Divide 6790 by 5")]
messages = react_graph.invoke({
    "messages": messages,
    "input_file": None
    })

# show the msgs
for m in messages['messages']:
    m.pre
