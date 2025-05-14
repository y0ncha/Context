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
2. splitting: chunk files using langchain docs splitter
                     |
                     v
3. embedding: embed chunks using openai embedder
                     |
                     v
4. vector store: create/load faiss vector store
                     |
                     v
5. retrieval: handle queries and retrieve top-k chunks
````

---

