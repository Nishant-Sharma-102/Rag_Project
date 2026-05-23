import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# =========================
# 🔹 Chunking Config
# =========================
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# =========================
# 🔹 Embedding Config
# =========================
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# =========================
# 🔹 Vector DB Config
# =========================
VECTOR_DB_PATH = "data/vector_db/faiss_index"
TOP_K = 5

# =========================
# 🔹 Groq LLM Config
# =========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

LLM_MODEL = "llama-3.1-8b-instant"   # or "llama3-70b-8192"
MAX_TOKENS = 500
TEMPERATURE = 0.2

# =========================
# 🔹 Prompt / RAG Controls
# =========================
MAX_CONTEXT_CHUNKS = 4   # limit docs sent to LLM