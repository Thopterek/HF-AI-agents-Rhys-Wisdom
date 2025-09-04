# -----------------------------
# Retrieval functions for Agent
# for more complex semantics:
# embedding-based retrievers
# like the one depended on:
# pip install sentence-transformers chromadb
# ------------------------------------------
from smolagents import Tool
# ------------------------------
# Old version kept commented out
# BM25 doesn't need embeddings
# from langchain_community.retrievers import BM25Retriever
# below the new version
# ---------------------
from sentence_transformers import SentenceTransformer
# getting the chroma to store the vectors
from langchain_chroma import Chroma
from langchain_core.documents import Document
# way to handle really long documents
from langchain.text_splitter import RecursiveCharacterTextSplitter

# creation of the tool
class GuestInfoRetrieverTool(Tool):
    name = "guest_info_retriever"
    description = """
    Retrieves detailed information about gala guests.
    The information is based on their names and relations.
    We get the information using a semanthing search.
    """
    inputs = {
            "query": {
                "type": "string",
                "description": """
                The name or the relation of the guest.
                Guest being the one you need information about.
                You can use natural language to describe the person
                """
                }
            }
    output_type = "string"

    def __init__(self, docs):
        # -------------------------
        # Old version commented out
        # -------------------------
        # self.is_intialized = False
        # self.retriever = BM25Retriever.from_documents(docs)
        # ------------------
        # initialize the embedding model
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        # spliting the document into smaller chunks for better retrieval
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        doc_chunks = text_splitter.split_documents(docs)
        # creation of the embedding and making a vectore store
        emeddings = LangChainEmbeddings(self.embedding_model)
        self.vectorstore = Chroma.from_documents(
                documents=doc_chunks,
                embedding=embeddings,
                collection_name="guest_info"
                )
        # retriving the objects from the vector store
        self.retriever = self.vectorstore.as_retriever(
                search_kwargs={"k": 3} # top 3 results
                )

    def forward(self, query: str):
        results = self.retriever.get_relevant_documents(query)
        if results:
            # -----------------------------------
            # small replacment no need for top :3
            # ------------------
            #return "\n\n".join(
            #        [doc.page_content for doc in results[:3]]
            #        )
            return "\n\n".join(
                    [doc.page_content for doc in results]
                    )
        else:
            return "No matching guest information found."

# --------------------------------------------------------------
# completly new class to adapt sentence transformer to LangChain
# --------------------------------------------------------------
class LangChainEmbeddings:
    def __init__(self, model):
        self.model = model
    def embed_documents(self, texts):
        return self.model.encode(texts).tolist()
    def embed_query(self, text):
        return self.model.encode(text).tolist()
# ---------------------
# initializing the tool
# not needed as it is in app.py
# guest_info_tool = GuestInfoRetrieverTool(docs)

