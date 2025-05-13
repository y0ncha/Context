# 📁 context-app – Project Structure

```text
context-app/
│
├── main.py                  # Streamlit/Gradio app entry point
├── config.py                # Model keys, constants, paths
├── .env                     # Environment variables
├── requirements.txt         # Python dependencies
│
├── ingestion/
│   ├── loader.py            # File loading using LangChain loaders
│   └── splitter.py          # Chunking using text splitters
│
├── embedding/
│   ├── embedder.py          # Embedding logic (OpenAI or local)
│   └── vector_store.py      # FAISS vector store creation/loading
│
├── retrieval/
│   └── retriever.py         # Query handling and top-k retrieval
│
├── generation/
│   └── rag_chain.py         # Prompt formatting + LLM call
│
├── ui/
│   └── interface.py         # UI layout and user interactions
│
└── utils/
    └── helpers.py           # Utilities: file renaming, extension checks, etc.
```

## 🔁 File Processing Pipeline
 1. **Loading:** Load files using LangChain loaders
 2. **Splitting:** Chunk files using text splitters
 3. **Embedding:** Embed chunks using OpenAI or local models
 4. **Vector Store:** Create/load FAISS vector store
 5. **Retrieval:** Handle queries and retrieve top-k chunks



---

## 🌱 Git Branching Strategy: Feature Development

```bash
# 1. Start from the development branch
git checkout dev

# 2. Create a new feature branch
git checkout -b feature/embedder

# 3. Work locally and commit often
git add .
git commit -m "Implemented Embedder class without persistence"

# 4. Push your branch to the remote
git push -u origin feature/embedder

# 5. Open a Pull Request to `dev` on GitHub/GitLab

# 6. Once approved, merge into `dev`

# 7. Periodically merge `dev` into `main` (add tags if needed)
