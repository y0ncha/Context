from pathlib import Path
from typing import List, Tuple, Optional
import os
from langchain.schema import Document
from langchain import document_loaders as dl
from config import MAX_FILE_SIZE


class LoadingError(Exception):
    """Custom exception for document loading errors."""
    pass


class FileLoader:
    """
    A document loader that handles multiple file formats using LangChain loaders.

    Supports PDF, DOCX, and PPTX files by default.
    You can customize the max file size or add more formats if needed.
    """


    def __init__(self, max_file_size: int = MAX_FILE_SIZE):
        """
        Initialize the loader with file size limit and supported extensions.
        """
        self.max_file_size = max_file_size # Maximum file size in bytes
        self.extensions = { # Dictionary of supported file extensions and their corresponding loaders
        ".pdf": dl.PyMuPDFLoader,
        ".docx": dl.UnstructuredWordDocumentLoader,
        ".pptx": dl.UnstructuredPowerPointLoader,
        }

    def load_documents(self, path_str: str) -> Tuple[List[List[Document]], List[Tuple[str, str]]]:
        """
        Load documents from a file or directory path.

        Args:
            path_str: Path to a file or directory containing documents.

        Returns:
            A tuple:
            - List of loaded documents (each element is a list of LangChain Document objects)
            - List of (filename, error message) tuples for failed loads

        Raises:
            FileNotFoundError: If the path doesn't exist
            LoadingError: If no files were successfully loaded
        """
        path = Path(path_str)
        docs: List[List[Document]] = []
        failed: List[Tuple[str, str]] = []

        if not path.exists():
            raise FileNotFoundError(f"Path not found: {path_str}")

        try:
            files = list(path.iterdir()) if path.is_dir() else [path]
        except Exception as e:
            raise LoadingError(f"Error accessing path: {e}")

        for file in files: # type: Path
            try:
                # If it's a directory, recursively load documents
                if file.is_dir():
                    sub_docs, sub_failed = self.load_documents(str(file))
                    docs.extend(sub_docs)
                    failed.extend(sub_failed)
                    continue

                # Validate the file before loading
                validation_error = self.validate_file(file)
                if validation_error:
                    failed.append((file.name, validation_error))
                    continue

                # Get file loader by extension
                file_loader = self.extensions.get(file.suffix.lower())

                # Load document using context manager
                with file_loader(str(file)) as doc_loader:
                        loaded = doc_loader.load()
                        docs.append(loaded)

            except Exception as e:
                failed.append((file.name, f"Unexpected error: {str(e)}"))

        if not docs and failed:
            raise LoadingError(f"Failed to load any documents. Errors: {failed}")

        return docs, failed

    def validate_file(self, file: Path) -> Optional[str]:
        """
        Validate a single file before loading.

        Args:
            file: Path object representing the file

        Returns:
            - None if the file is valid
            - A string with an error message if the file is invalid
        """
        if not file.exists():
            return "File does not exist"
        if not file.is_file():
            return "Not a regular file"
        if not os.access(file, os.R_OK):
            return "File is not readable"
        if file.suffix.lower() not in self.extensions:
            return f"Unsupported file format: {file.suffix}"
        if file.stat().st_size > self.max_file_size:
            return f"File exceeds maximum size of {self.max_file_size} bytes"
        return None