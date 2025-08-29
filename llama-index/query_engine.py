# ---------------------------
# Querying a VectorStoreIndex
# ---------------------------
from llama_index.llms.huggingface_api import HuggingfaceInferenceAPI

llm = HuggingfaceInferenceAPI(model_name="Qwen/Qwen2.5-Coder-32B-Instruct")
query_engine = index.as_query_engine(
        llm=llm,
        response_mode="tree_summarize"
        )
query_engine.query("What is the meaning of life?")

# ------------------------------
# And adding the evaluation part
# ------------------------------
from llama_index.core.evaluation import FaithfulnessEvaluator

evaluator = FaithfulnessEvaluator(llm=llm)
respone = qury_engine.query("What battles took place in NYC in the American Revolution?")
eval_result = evaluator.evaluate_response(response=response)
eval_result.passing
