# -----------------------------------
# Example of creating a workflow loop
# based to be run on the hints we give
# ------------------------------------
from llama_index.core.workflow import Event
import random
# -------------------------------------------------
# Option to draw the workflows through an HTML file
# -------------------------------------------------
from llama_index.utils.workflow import draw_all_possible_flows
# -------------------------------------------------------------
# and now the way to control manage the state, as per the rule:
# every step has access to the same state by using the Context
# -------------------------------------------------------------
from llama_index.core.workflow import Context, StartEvent, StopEvent

# the prototype of the step function
@step
async def query(self, ctx: Context, ev: StartEvent) -> StopEvent:
    # store the query inside the Context
    await ctx.store.set("query", "What is the capital of Germany")
    # do something with context and Event
    val = ...
    # retrive query from the Context
    query = await ctx.store.get("query")
    return StopEvent(result=val)

class ProcessingEvent(Event):
    intermediate_result: str

class LoopEvent(Event):
    loop_output: str

class MultiStepWorkflow(Workflow):
    @step
    async def step_one(self, ev: StartEvent | LoopEvent) -> ProcessingEvent | LoopEvent:
        if random.randint(0, 1) == 0:
            print("Bad things happened")
            return LoopEvent(loop_output="Back to step one")
        else:
            print("Good things happened")
            return ProcessingEvent(intermediate_result="First step completed")

    @step
    async def step_two(self, ev: ProcessingEvent) -> StopEvent:
        # Use the intermediate_result
        final_result = f"Finished processing: {ev.intermediate_result}"
        return StopEvent(result=final_result)

work = MultiStepWorkflow(verbose=False)
# -------------------------------------
# Actual call to draw the thing in html
# -------------------------------------
draw_all_possible_flows(work, flow.html)
result = await work.run()
result
