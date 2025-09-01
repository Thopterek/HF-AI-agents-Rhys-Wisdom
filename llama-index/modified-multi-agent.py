# -----------------------------------
# Version with function call counters
# using the context state for workflow
# ------------------------------------
from llama_index.core.workflow import Context

# define some tools
async def add(ctx: Context, a: int, b: int) -> int:
    """
    Adding two numbers and getting the result of sum
    """
    curr_state = await ctx.store.get("state")
    curr_state["num_fn_calls"] += 1
    await ctx.store.set("state", curr_state)
    return a + b

async def multiply(ctx: Context, a: int, b: int) -> int:
    """
    Multiply two numbers and get the result
    """
    curr_state = await ctx.store.get("state")
    curr_state["num_fn_calls"] += 1
    await ctx.store.set("state", curr_state)
    return a * b

# -----

workflow = AgentWorkflow(
        agents=[multiply_agent, addition_agent],
        root_agent="multiply_agent",
        initial_state={"num_fn_calls": 0},
        state_prompt="Current state: {state}. User message: {msg}"
        )
# running the workflow with context
ctx = Context(workflow)
response = await workflow.run(user_msg="Can you add 5 and 3", ctx=ctx)

# pulling out and inspecting the state
state = await ctx.store.get("state")
print(state["num_fn_calls"])

