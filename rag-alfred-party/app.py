# --------------------------------
# Integrating the Tools with Agent
# --------------------------------
from smolagents import CodeAgent, InferenceClientModel
# importing entire modules with the code
import retriever, tools

# Initialize the HF model
model = InferenceClientModel()

# Alfred our gala agent with guest info tool
alfred = CodeAgent(tools=[guest_info_tool], model=model)

# Example query for Alfred
response = alfred.run("Tell me about our guest Lady Ada Lovelace.")

print("Alfred responds with:")
print(response)
