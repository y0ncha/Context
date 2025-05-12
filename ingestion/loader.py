import os
os.environ["OPENAI_API_KEY"] = "key"

from langchain.document_loaders import (
    PyPDFLoader as pdf_loader,
    Docx2txtLoader as docx_loader,
    UnstructuredPowerPointLoader as pptx_loader,
)
