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
---

## 🔁 file processing pipeline
````
1. loading: load files using langchain loaders
                     |
                     v
2. splitting: chunk files using text splitters
                     |
                     v
3. embedding: embed chunks using openai or local models
                     |
                     v
4. vector store: create/load faiss vector store
                     |
                     v
5. retrieval: handle queries and retrieve top-k chunks
````

---

## 🌱 git branching strategy: feature development

```
1. The dev branch acts as the integration branch – all new features are based on it, tested together, and later merged into main.

2. Each feature is developed in its own branch, named like feature/embedder, to keep changes isolated and focused.

3. Developers work and commit locally on their feature branches during development.

4. When a feature is ready, a pull request is opened targeting the dev branch.

5. After review and approval, the feature branch is merged into dev.

6. Periodically, the dev branch is merged into main, the stable production branch. Version tags may be added at this point for release tracking.