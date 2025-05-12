# 🧠 Context – Your AI Powered Study Assistant

**Context** is a local AI assistant for students. It lets you upload your study materials (PDFs, slides, notes) and ask natural language questions about them. Powered by LangChain, FAISS, and modern LLMs, Context gives grounded answers based on your files — with full privacy and local control.

---

## 🚀 Features

- 📥 Upload PDFs, DOCX, TXT, or Markdown files
  
- ✂️ Automatically splits documents into semantic chunks
  
- 🔢 Embeds content with OpenAI or local models
  
- 📚 Stores vectors in FAISS for fast local retrieval
  
- 🔍 Ask questions in plain English, get answers based on your data
  
- 🧠 Powered by Retrieval-Augmented Generation (RAG)

- 💻 Simple UI built with Streamlit or Gradio

---

## 📦 Tech Stack

| Component        | Tool/Library                    |
|------------------|----------------------------------|
| File Handling    | `LangChain.document_loaders`     |
| Chunking         | `RecursiveCharacterTextSplitter` |
| Embeddings       | `OpenAIEmbeddings`, `HuggingFaceEmbeddings` |
| Vector Store     | `FAISS`                          |
| Language Models  | `OpenAI`, `local LLMs via Ollama` |
| UI               | `Streamlit` or `Gradio`          |

---

<pre>
context-app/
├── main.py                  # App entry point
├── config.py                # API keys, constants
├── requirements.txt         # Dependencies
│
├── ingestion/               # File loading & chunking
│   ├── loader.py
│   └── splitter.py
│
├── embedding/               # Embedding and vector store
│   ├── embedder.py
│   └── vector_store.py
│
├── retrieval/               # Chunk retriever
│   └── retriever.py
│
├── generation/              # Prompt + LLM logic
│   └── rag_chain.py
│
├── ui/                      # User interface
│   └── interface.py
│
└── utils/                   # Helper functions
    └── helpers.py
</pre>


---

## ⚡ Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/context-app.git
cd context-app

### 2. Install dependencies
pip install -r requirements.txt

### 3. Add your OpenAI key (or use a local model)
in config.py OPENAI_API_KEY = "your-key-here"

###4. Run the app
streamlit run main.py
