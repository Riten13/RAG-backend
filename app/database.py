import chromadb
from app.config import settings
from chromadb.utils import embedding_functions


embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)


_chroma_client = chromadb.CloudClient(
    api_key=settings.CHROMA_API_KEY,
    tenant=settings.CHROMA_TENANT,
    database=settings.CHROMA_DATABASE
)
_collection = _chroma_client.get_or_create_collection(name="file_metadata",embedding_function=embedding_fn)

def get_chroma_client():
    return _chroma_client

def get_collection():
    return _collection

