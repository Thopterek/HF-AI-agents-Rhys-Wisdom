# ---------------------------------------------------------------
# My solution for the Quiz question one which should have:
# - Correct imports are included
# - DuckDuckGoSearchTool is added to tools list
# - HfApiModel is configured
# - Model ID is correctly specified
# ---------------------------------------------------------------
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

choosen_model = HfApiModel(model_id = "Qwen/Qwen2.5-Coder-32B-Instruct")
search = DuckDuckGoSearchTool()

agent = CodeAgent(
        tools=[search],
        model=choosen_model
        )
# ------------------------
# The solution from the HF
# ------------------------
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel

agent = CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")
        )
