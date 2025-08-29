# ----------------------------------------
# Second question about Multi-Agent System
# which should have:
# - Web agent has correct tools configured
# - Manager agent references web agent
# - Appropriate max_steps value is set
# - Required imports are authorized
# ----------------------------------------
from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, ToolCallingAgent 

choosen_model = HfApiModel(model_id = "Qwen/Qwen2.5-Coder-32B-Instruct")
search = DuckDuckGoSearchTool()
# Create web agent and manager agent structure
web_agent = ToolCallingAgent(
    tools=[search],           # Add required tools
    model=choosen_model,         # Add model
    max_steps=6,        # Adjust steps
    name="web_searching_agent",           # Add name
    description="Agent is using basic model Qwen2.5-Coder-32B-Instruct and DuckDuckGoSearchTool"      # Add description
)

manager_agent = CodeAgent(
        tools=[web_agent]
        model=choosen_model,
        max_steps=4,
        name="manager_agent",
        description="Agent that is giving task to another agents coordinating their tasks like websearch"
        )

# ----------------
# Solution from HF
# ----------------
web_agent = ToolCallingAgent(
        tools=[DuckDuckGoSearchTool(), visit_webpage],
        model=model,
        max_steps=10,
        name="search",
        description="Runs web searches for you."
        )

manager_agent = CodeAgent(
        tools=[],
        model=model,
        managed_agents=[web_agent],
        additional_authorized_imports=["time", "numpy", "pandas"]
        )

