# ------------------------------------------------------------------
# The first example on how to connect to the Llama llama_index
# depends on the following:
# pip install llama-index-llms-huggingface-api llama-index-embeddings-huggingface
# testing the connection
# ------------------------------------------------------------------
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
import os
from dotenv import load_dotenv

load_dotenv()

hf_token = os.getenv("HF_TOKEN")

llm = HuggingFaceInferenceAPI(
        model_name="Qwen/Qwen2.5-Coder-32B-Instruct",
        temperature=0.7,
        max_tokens=100,
        token=hf_token,
        provider="auto"
        )
response = llm.complete("Hello, how are you?")
print(response)
