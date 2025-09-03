# -----------------------------
# Retrieval functions for Agent
# for more complex semantics:
# embedding-based retrievers
# -----------------------------
from smolagents import Tool
# BM25 doesn't need embeddings
from langchain_community.retrievers import BM25Retriever

# creation of the tool
class GuestInfoRetrieverTool(Tool):
    name = "guest_info_retriever"
    description = """
    Retrieves detailed information about gala guests.
    The information is based on their names and relations.
    """
    inputs = {
            "query": {
                "type": "string",
                "description": """
                The name or the relation of the guest.
                Guest being the one you need information about.
                """
                }
            }
    output_type = "string"

    def __init__(self, docs):
        self.is_intialized = False
        self.retriever = BM25Retriever.from_documents(docs)

    def forward(self, query: str):
        results = self.retriever.get_relevant_documents(query)
        if results:
            return "\n\n".join(
                    [doc.page_content for doc in results[:3]]
                    )
        else:
            return "No matching guest information found."

# initializing the tool
guest_info_tool = GuestInfoRetrieverTool(docs)

