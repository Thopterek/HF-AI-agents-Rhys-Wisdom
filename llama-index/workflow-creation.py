# ------------------------------------------------
# Basic Worflow Creation depending on the package:
# pip install llama-index-utils-workflow
# ------------------------------------------------
from llama_index.core.workflow import StartEvent, StopEvent, Workflow, step

# -------------------------
# defining of the workflow
# with using decorator for step
# -----------------------------
class MyWorkFlow(Workflow):
    @step
    async def my_step(self, ev: StartEvent) -> StopEvent
        # do something here
        return StopEvent(result="Hello, everyone!")

# actually making it run
work = MyWorkFlow(timeout=10,
                  verbose=False)
result = await work.run()
# -------------------------
# Connecting Multiple Steps
# type hinting for correct execution
# -----------------------------------
from llama_index.core.workflow import Event

class ProcessingEvent(Event):
    intermediate_result: str

class MultiStepWorkflow(Workflow):
    @step
    async def step_one(self, ev: StartEvent) -> ProcessingEvent:
        # process initial data
        return ProcessingEvent(intermediate_result="Step 1 complete")
    @step
    async def step_two(self, ev: ProcessingEvent) -> StopEvent:
        # use of intermediate result
        final = f"Finished processing: {ev.intermediate_result}"
        return StopEvent(result=final_result)

work = MultiStepWorkflow(timeout=10, verbose=False)
result = await work.run()
result

