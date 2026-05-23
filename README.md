# ⚡ AETHER SPACE

**Aether Space** is a state-of-the-art, high-performance Retrieval-Augmented Generation (RAG) chatbot designed to ingest documents (PDFs and CSVs) and answer user queries with extreme accuracy and deep context.

Featuring a beautiful, custom dark-themed interactive Streamlit interface, Aether Space leverages a hybrid search pipeline, reciprocal rank fusion, and a cross-encoder reranker to supply the LLM with the most relevant information possible.

---

## 🚀 Key Features

*   **🌌 Stunning Dark Mode UI:** A fully custom space-themed Streamlit user interface featuring interactive micro-animations and glowing visual elements.
*   **📁 Multi-format Document Ingestion:** Support for PDF and CSV document uploads with automatic token splitting.
*   **🔍 Hybrid Search Engine:** Combines **Dense Retrieval** (FAISS Vector Store powered by Sentence Transformers) with **Sparse Retrieval** (BM25) to catch both semantic meaning and keyword matches.
*   **🔄 Advanced Query Processing:** Automatic **Query Rewriting** and **Query Expansion** to find relevant info even if the question is phrased differently.
*   **⚡ Reciprocal Rank Fusion (RRF):** Intelligently merges retrieval results from both dense and sparse sources.
*   **🎯 Cross-Encoder Reranking:** Re-evaluates search results using a cross-encoder model (`ms-marco-MiniLM-L-6`) to select the highest-quality context chunks.
*   **🧠 Groq Inference Acceleration:** Powered by Llama 3 models via Groq API for near-instantaneous responses.

---

## 🛠️ Project Structure

```text
├── app/
│   ├── main.py                 # Streamlit entry point (Aether Space interface)
│   └── main_aether.py          # Backup application file
├── core/
│   └── config.py               # Settings for Chunking, Vector DB, and LLM configuration
├── generation/
│   ├── llm.py                  # Groq client configuration & call function
│   └── prompt_builder.py       # Context assembly & system prompt construction
├── indexing/
│   ├── dense_index.py          # FAISS Dense vector database creation & loader
│   └── sparse_index.py         # BM25 Sparse index creation
├── pipeline/
│   └── rag_pipeline.py         # Complete Ingestion & RAG query pipelines
├── ranking/
│   └── reranker.py             # CrossEncoder context reranker
├── retrieval/
│   ├── hybrid_retriever.py     # Executes dense and sparse searches
│   ├── query_expansion.py      # Generates query variations for better coverage
│   ├── query_rewriter.py       # Rewrites user input for optimal retrieval
│   └── rrf_fusion.py           # Reciprocal Rank Fusion algorithm
├── services/
│   ├── csv_loader.py           # Processes CSV documents
│   ├── pdf_loader.py           # Parses PDF documents
│   ├── text_splitter.py        # Tokenizer-based text splitter
│   └── context_compressor.py   # Compresses documents to fit within token limit
└── requirements.txt            # Python package dependencies
```

---

## 💻 Getting Started

Follow these steps to run the project on your machine.

### Prerequisites
Make sure you have **Python 3.10+** installed.

### 1. Clone & Navigate to Project
Open your terminal and navigate to the project directory:
```bash
cd "c:/Users/nisha/Downloads/chat_boot_projects (1)/chat_boot_projects"
```

### 2. Install Dependencies
It is highly recommended to use the included virtual environment (`.venv`). If you need to reinstall packages:
```bash
.\.venv\Scripts\pip install -r requirements.txt
```

### 3. Run the Application
Start the Streamlit application using the local environment's python package:

```powershell
.\.venv\Scripts\streamlit run app/main.py
```

After executing, Streamlit will automatically open in your browser at:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 📖 How to Use Aether Space

1.  **Open the Sidebar:** Click the sidebar toggle in the top left corner.
2.  **Upload Knowledge Documents:** Drag and drop one or more `.pdf` or `.csv` files.
3.  **Choose File Type:** Select the matching file format from the dropdown menu.
4.  **Ingest Data:** Click the **🚀 Ingest Data** button. This splits, embeds, and indexes your files locally.
5.  **Chat:** Ask your question in the chat input field at the bottom.
6.  **Debug Mode (Optional):** Expand the `🔍 Debug Info` accordion in the chat to see how your query was rewritten, expanded, and retrieved!
