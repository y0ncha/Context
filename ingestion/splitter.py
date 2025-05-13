from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from config import CHUNK_SIZE, CHUNK_OVERLAP
from typing import List

class FileSplitter:
    """
    A document splitter that breaks documents into overlapping chunks
    using LangChain's RecursiveCharacterTextSplitter.

    Attributes:
        chunk_size (int): Max number of characters per chunk.
        chunk_overlap (int): Number of characters of overlap between chunks.
    """

    def __init__(self, chunk_size: int = CHUNK_SIZE, chunk_overlap: int = CHUNK_OVERLAP):
        """
        Initialize the text splitter with chunking configuration.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap
        )

    def split_documents(self, docs: List[Document]) -> List[Document]:
        """
        Splits a list of LangChain Document objects into overlapping text chunks.

        Args:
            docs: A list of LangChain Documents.

        Returns:
            A flat list of Document chunks (also LangChain Document objects).
        """
        return self.text_splitter.split_documents(docs)