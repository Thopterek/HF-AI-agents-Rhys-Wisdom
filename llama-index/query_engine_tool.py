# ----------------------------------------------------------------
# A base for QueryEngineTool transfroming the standard QueryEngine
# ----------------------------------------------------------------
from llama_index.core import VectorStoreIndex
from llama_index.core.tools import QueryEngineTool
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI 
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

embed = HuggingFaceEmbedding("BAAI/bge-small-en-v1.5")
db = chromadb.PersistentClient(path="./alfred_chroma_db")
collection = db.get_or_create_collection("alfred")
vector_store = ChromaVectorStore(chroma_collection=collection)

index = VectorStoreIndex.from_vector_store(vector_store, embed_model=embed)
llm = HuggingFaceInferenceAPI(model_name="Qwen/Qwen2.5-Coder-32B-Instruct")
query_engine = index.as_query_engine(llm=llm)
tool = QueryEngineTool.from_default(query_engine, name="Nice-name", description="and description")
