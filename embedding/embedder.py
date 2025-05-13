from typing import List
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document


class FileEmbedder:
    """
    A text embedding handler using OpenAI (or other) backends via LangChain.

    Converts text chunks into vector embeddings for semantic search.
    """

    def __init__(self, model_name: str = "openai"):
        if model_name == "openai":
            self.embedding_model = OpenAIEmbeddings()
        else:
            raise ValueError(f"Unsupported embedding model: {model_name}")

    def embed(self, docs: List[Document]) -> FAISS:
        """
        Converts a list of Documents into vector embeddings using the selected backend.

        Args:
            docs: A list of LangChain Document objects to embed.

        Returns:
            A FAISS vectorstore object containing all embedded documents (in-memory).
        """
        return FAISS.from_documents(docs, self.embedding_model)