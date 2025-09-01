# ------------------------------
# The base for the LangGraph app
# ------------------------------
from typing_extenstions import TypedDict

# getting data to go through nodes
class State(TypedDict):
    graph_state: str

# actual nodes used
def node_one(state):
    print("NODE ONE CALLED")
    return {"graph_state": state['graph_state'] + " I am"}

def node_two(state):
    print("NODE TWO")
    return {"graph_state": state['graph_state'] + " happy!"}

def node_three(state):
    print("N O D E - 3")
    return {"graph_state": state['graph_state'] + " sad..."}

# edges to connect them
import random
from typing import Literal

def decide_mood(state) -> Literal["node_2", "node_3"]:
    # using the state to decide what node to visit
    user_input = state['graph_state']
    # getting the random split between nodes
    if random.random() < 0.5:
        return "node_2"
    return "node_3"

# and creation of StateGraph that holds the workflow
from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

# bulding of the graph
builder = StateGraph(State)
builder.add_node("node-1", node_one)
builder.add_node("node-2", node_two)
builder.add_node("node-3", node_three)

# creating a logic for it
builder.add_edge(START, "node-1")
builder.add_conditional_edges("node-1", decide_mood)
builder.add_edge("node-2", END)
builder.add_edge("node-3", END)

# Putting it together
graph = builder.compile()

# and the visualize it
display(Image(graph.get_graph().draw_mermaid_png()))

# or/and invoke it
graph.invoke({"graph_state" : "Hi, this is me."})

