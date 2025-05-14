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

    def embed(self, chunks: List[Document]) -> FAISS:
        """
        Converts a list of Documents into vector embeddings using the selected backend.

        Args:
            chunks: A list of LangChain Document objects to embed.

        Returns:
            A FAISS vectorstore object containing all embedded documents (in-memory).
        """
        
        if not chunks:
            raise ValueError("No documents were provided to embed.")

        payloads = [chunk.page_content for chunk in chunks]
        embeddings = self.embedding_model.embed_documents(payloads)

        if not embeddings:
            raise ValueError("Failed to generate embeddings for the provided documents.")
        if len(embeddings) != len(chunks):
            raise ValueError("Mismatch between number of documents and embeddings generated.")

        return embeddings