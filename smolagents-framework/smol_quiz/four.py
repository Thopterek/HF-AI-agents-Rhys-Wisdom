# ------------------------------------------------
# The assingment goes as follows:
# - Tools are properly configured
# - Step limit is set appropriately
# - Agent name and description are provided
# - Basic configuration is complete
# ------------------------------------------------
from smolagents import ToolCallingAgent, HfApiModel
from smolagents.tools import tool

@tool
def add_numbers(first_number: int, second_number: int) -> int:
    """
    Args:
        first_number: any possible integer value from INTMIN to INTMAX
        second_number: any possible integer value from INTMIN to INTMAX
    Return value:
        Integer value that is the sum of those two numbers
    """
    result = first_number + second_number
    return result

choosen_model = HfApiModel(model_id = "Qwen/Qwen2.5-Coder-32B-Instruct")

agent = ToolCallingAgent(
        tools=[add_numbers],
        model=choosen_model,
        max_steps=4,
        name="tool_agent",
        description="Agent has access to add_numbers tool to help and solve the task of adding two numbers"
        )
# ------------
# HF solution:
# ------------
from smolagents import ToolCallingAgent

agent = ToolCallingAgent(
        tools=[custom_tool],
        model=model,
        max_steps=5,
        name="tool agent",
        description="Executes specific tools based on input"
        )

