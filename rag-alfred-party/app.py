# --------------------------------
# Integrating the Tools with Agent
# to test we would need to add
# model_id = "choosen model"
# token = os.getenv("HF_TOKEN")
# --------------------------------
from smolagents import CodeAgent, InferenceClientModel
# importing entire modules with the code
# and then changing to be only things needed
from retriever import GuestInfoRetrievalTool
from tools import docs
import os

# Initialize the HF model
model = InferenceClientModel()

# intiialize the tools and documents
guest_info_tool = GuestInfoRetrievalTool(docs)
# Alfred our gala agent with guest info tool
alfred = CodeAgent(
        tools=[guest_info_tool],
        model=model,
        system_promt="""
        You are Alfred, the helpful assistant for high profile Gala.
        Use the guest_info_retriever tool to look up the informations about guests.
        Always be polite and try your best to be as truthful as possible.
        """)

# Example query for Alfred
response = alfred.run("Tell me about our guest Lady Ada Lovelace.")

print("Alfred responds with:")
print(response)
