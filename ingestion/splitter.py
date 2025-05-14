from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from config import CHUNK_SIZE, CHUNK_OVERLAP
from typing import List
from pathlib import Path
import re

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
        if not docs:
            raise ValueError("No documents were provided to split.")

        try:
            chunks = self.text_splitter.split_documents(docs)
        except Exception as e:
            raise ValueError(f"Error splitting documents: {e}")

        # Add id, token count and weight (priority) in the to each chunk metadata
        for i, chunk in enumerate(chunks):
            try:
                chunk.metadata["chunk_id"] = self.id_chunk(chunk, i)
                chunk.metadata["token_count"] = len(chunk.page_content.split())
                chunk.metadata["weight"] = 1.0  # default weight value (can be adjusted later)
            except Exception as e:
                raise ValueError(f"Error adding metadata to chunk No.{i}: {e}")

        if not chunks:
            raise ValueError("No chunks were generated after splitting.")
        return chunks

    def id_chunk(self, doc: Document, idx: int) -> str:
        """
        Generate a clean identifier for a document chunk by removing file extension
        and replacing whitespace with underscores.

        Args:
            doc: A LangChain Document object.
            idx: The index of the chunk in the list of chunks.

        Returns:
            A sanitized string identifier.
        """
        try:
            # Extract the source filename from metadata
            source = doc.metadata.get("source", "unknown")

            # Get the filename without the extension
            file_name = Path(source).stem  # Using stem to get the name without extension

            # First, replace whitespace with underscores
            file_name = file_name.replace(" ", "_")  # Replace spaces with underscores

            # Replace whitespace with underscores
            clean_id = re.sub(r'[^\w\-]', '_', file_name)

            # Append the index to the clean ID
            clean_id += f"_{idx:03}"

        except Exception as e:
            raise ValueError(f"Error generating chunk ID: {e}")

        return clean_id
