# ----------------------------------------------------
# Setting up Model Integration: Question 5 from Quiz
# - Correct model imports are included
# - Model is properly initialized
# - Model ID is correctly specified
# - Alternative model option is provided
# ----------------------------------------------------
from smolagents import HfApiModel, InferenceClientModel

model = HfApiModel(model_id = "HuggingFaceH4/zephyr-7b-beta")

alter_model = InferenceClientModel()
# --------------
# Thier solution
# --------------
from smolagents import HfApiModel, LiteLLMModel

hf_model = HfApiModel("Qwen/Qwen2.5-Coder-32B-Instruct")
other_model = LiteLLMModel("anthropic/claude-3-sonnet")
