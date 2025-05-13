# 📁 context-app – project structure

```TEXT
context-app/
│
├── main.py                  # streamlit/gradio app entry point
├── config.py                # model keys, constants, paths
├── .env                     # environment variables
├── requirements.txt         # python dependencies
│
├── ingestion/
│   ├── loader.py            # file loading using langchain loaders
│   └── splitter.py          # chunking using text splitters
│
├── embedding/
│   ├── embedder.py          # embedding logic (openai or local)
│   └── vector_store.py      # faiss vector store creation/loading
│
├── retrieval/
│   └── retriever.py         # query handling and top-k retrieval
│
├── generation/
│   └── rag_chain.py         # prompt formatting + llm call
│
├── ui/
│   └── interface.py         # ui layout and user interactions
│
└── utils/
    └── helpers.py           # utilities: file renaming, extension checks, etc.
```

## 🔁 file processing pipeline
 1. **loading:** load files using langchain loaders
 2. **splitting:** chunk files using text splitters
 3. **embedding:** embed chunks using openai or local models
 4. **vector store:** create/load faiss vector store
 5. **retrieval:** handle queries and retrieve top-k chunks



---

## 🌱 git branching strategy: feature development

```bash
# 1. start from the development branch
git checkout dev

# 2. create a new feature branch
git checkout -b feature/embedder

# 3. work locally and commit often
git add .
git commit -m "implemented embedder class without persistence"

# 4. push your branch to the remote
git push -u origin feature/embedder

# 5. open a pull request to `dev` on github/gitlab

# 6. once approved, merge into `dev`

# 7. periodically merge `dev` into `main` (add tags if needed)
