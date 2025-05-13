import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# === API Keys ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# === Splitter Config ===
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# === Loader Config ===
MAX_FILE_SIZE = 100 * 1024 * 1024  # 100MB

# === Embedding Model ===
EMBEDDING_MODEL = "openai"  # Currently only OpenAI is supported