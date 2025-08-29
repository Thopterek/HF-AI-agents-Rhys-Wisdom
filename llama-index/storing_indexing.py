# -------------------------------
# Using Chroma to store documents
# -------------------------------
import chromadb
from llama_index.vector_stores.chrom import ChromaVectorStore

db = chromadb.PersistentClient(path="./alfred_chroma_db")
chroma_c = db.get_or_create_collection("alfred")
vector = ChromaVectorStore(chroma_collection=chroma_collection)

pipe = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=25, chunk_overlap=0),
            HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
            ],
        vector_store=vector
        )
# -----------------------------------------------
# creating index from vector store and embeddings
# -----------------------------------------------
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
index = VectorStoreIndex.from_vector_store(vector_store, embed_model=embed_model)

