# ------------------------------------------------------------------
# Simple ReAct loop agent, definitng set of fns/tools that define it
# ------------------------------------------------------------------
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.core.tools import FunctionTool

# sample tool definition:
def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers and returns the resulting integer
    """
    return a * b

# initialization of llm
model = HuggingFaceInferenceAPI(model_name="Qwen/Qwen2.5-Coder-32B-Instruct")

# initialize agent
agent = AgentWorkflow.from_tools_or_functions(
        [FunctionTool.from_defaults(multiple)],
        llm=model
        )

# stateless
# ----------
# being also asynchronus (await operator)
# await returns coroutine instead of executing
# pausing the execution until the task is done
# --------------------------------------------
response = await agent.run("What is 2 times 2")

# remembering state
from llama_index.core.workflow import Context

memory = Context(agent)

response = await agent.run("My name is Bob.", ctx=memory)
response = await agent.run("What was my name again?", ctx=memory)

# ------------------------------------------------------
# Agentic RAG version would need the following additions
# ------------------------------------------------------
from llama_index.core.tools import QueryEngineTool

# similarity_top_k is taken from Components in llama
engine = index.as_query_engine(llm=model, similarity_top_k=3)

query_engine_tool = QueryEngineTool.from_defaults(
        query_engine=engine,
        name="name",
        description="a specific description",
        return_direct=False
        )
query_agent = AgentWorkflow.from_tools_or_functions(
        [query_engine_tool],
        llm=model,
        system_prompt="You are a: Helpful assistant that has access to a database"
        )
