# --------------------------------------------------------
# Multi-Agent system with simple tools for showcase
# --------------------------------------------------------
from llama_index.core.agent.workflow import (AgentWorkflow,
                                             FUnctionAgent,
                                             ReActAgent
                                             )
# two simple tools
def add(a: int, b: int) -> int:
    """
    Addition of two numbers returns their sum
    """
    return a + b

def substract(a: int, b: int) -> int:
    """
    Substract two numbers and return new value
    """
    return a - b

# Agents configs
# FunctionAgent - work with LLMs with fn calling API
# or
# ReActAgent - working with any LLM
calc_agent = ReActAgent(
        name="calculator",
        description="Basic arithmetic operations",
        system_prompt="You are a calculator assistant, use any tools for any calculations",
        tools=[add, substract],
        llm=llm # to be defined actually
        )
query_agent = ReActAgent(
        name="info_lookup",
        description="Looks up information about XYZ",
        system_prompt="Use your tool to query a RAG system to answer informations about XYZ"
        tools=[query_engine_tool], # and similiar to this one
        llm=llm # once again
        )
# Creating and running the workflow
agent = AgentWorkflow(
        agents=[calc_agent, query_agent],
        root_agent="calculator"
        )
# Running it
response = await agent.run(user_msg="Can you add 5 and 3?")

