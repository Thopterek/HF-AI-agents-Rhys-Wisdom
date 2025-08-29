# ------------------------------------
# Continuation of creating a reference
# - E2B sandbox is configured
# - Authorized imports are limited
# - Security settings are implemented
# - Basic agent configuration
# ------------------------------------
from smolagents import CodeAgent, HfApiModel
from smolagents.tools import E2BSandboxTool

chosen_model = HfApiModel(model_id="HuggingFaceH4/zephyr-7b-beta")

e2b = E2BSandboxTool(
        allowed_imports=["math", "json"],
        timeout=30
        )

agent = CodeAgent(
        tools=[e2b],
        model=chosen_model
        )
# -----------------------------
# Their solution to the problem
# -----------------------------
from smolagents import CodeAgent, E2BSandboxTool

agent = CodeAgent(
        tools=[],
        model=model,
        sandbox=E2BSandbox(),
        additional_authorized_imports=["numpy"]
        )
