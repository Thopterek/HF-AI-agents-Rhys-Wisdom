# -----------------------------------------
# Creating the auxilary tools for the agent
# combination of smolagents & langgraph
# -----------------------------------------
import datasets
from langchain_core.documents import Document

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

