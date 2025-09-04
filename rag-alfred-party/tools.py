# -----------------------------------------
# Creating the auxilary tools for the agent
# combination of smolagents & langgraph
# -----------------------------------------
import datasets
from langchain_core.documents import Document
from smolagents import Tool

# loading of the dataset
guest_dataset = datasets.load_dataset(
        "agents-course/unit3-invitees",
        split="train")

# conversion of dataset entries into Document objects
docs = [
        Document(
            page_content="\n".join([
                f"Name: {guest['name']}",
                f"Relation: {guest['relation']}",
                f"Description: {guest['description']}",
                f"Email: {guest['email']}"
                ]),
            metadata={"name": guest["name"]}
            )
        for guest in guest_dataset
        ]

# memory tool that helps to keep the conversation flow
class GuestMemory(tool):
   name="guest_memory_for_conversation",
   description="""
   This tool allows to sort with whom Alfred had conversation.
   Thanks to that better allowing him to respond as he remembers about what it was.
   Everything is being saved in a structure to check per key: name, value: conversation
   """,
   inputs={
           "query with new conversation" {
               "type": "string",
               "input": "string, being the name of the guest that Alfred makes conversation with",
               "output": "string with all the prior prompts / conversation that he had"
               }
           }
   output_type = "string"
   #def __init__(self)
   # TBD there is a question of available options to test in closed up env
