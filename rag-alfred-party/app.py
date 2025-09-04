# --------------------------------
# Integrating the Tools with Agent
# --------------------------------
from smolagents import CodeAgent, InferenceClientModel
# importing entire modules with the code
# and then changing to be only things needed
from retriever import GuestInfoRetrievalTool
from tools import docs

# Initialize the HF model
model = InferenceClientModel()

# intiialize the tools and documents
guest_info_tool = GuestInfoRetrievalTool(docs)
# Alfred our gala agent with guest info tool
alfred = CodeAgent(tools=[guest_info_tool], model=model)

# Example query for Alfred
response = alfred.run("Tell me about our guest Lady Ada Lovelace.")

print("Alfred responds with:")
print(response)
