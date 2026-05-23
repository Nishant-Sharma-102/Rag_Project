import streamlit as st

from services.pdf_loader import load_pdf
from services.csv_loader import load_csv
from services.text_splitter import split_documents
from services.context_compressor import compress_documents

from indexing.dense_index import create_faiss_index, load_faiss_index
from indexing.sparse_index import create_bm25_index

from retrieval.query_rewriter import rewrite_query
from retrieval.query_expansion import expand_query
from retrieval.hybrid_retriever import hybrid_retrieve
from retrieval.rrf_fusion import rrf_fusion

from ranking.reranker import rerank

from generation.prompt_builder import build_prompt
from generation.llm import generate_answer

from core.config import MAX_CONTEXT_CHUNKS


# =========================
# 🔹 Ingestion Pipeline
# =========================
def ingest_data(uploaded_file, file_type):
    if file_type == "pdf":
        docs = load_pdf(uploaded_file)
    elif file_type == "csv":
        docs = load_csv(uploaded_file)
    else:
        raise ValueError("Unsupported file type")

    chunks = split_documents(docs)

    # Dense index
    create_faiss_index(chunks)

    # Sparse index
    bm25, documents = create_bm25_index(chunks)

    # Store in session
    st.session_state.bm25 = bm25
    st.session_state.documents = documents

    st.success("✅ Data indexed successfully!")


# =========================
# 🔹 RAG Chat Pipeline
# =========================
def rag_chat(query):
    vectorstore = load_faiss_index()

    # Safety check
    if "bm25" not in st.session_state or "documents" not in st.session_state:
        st.error("⚠️ Please ingest data first.")
        return None, []

    bm25 = st.session_state.bm25
    documents = st.session_state.documents

    # Step 1: Rewrite
    rewritten_query = rewrite_query(query)

    # Step 2: Expand
    expanded_queries = expand_query(rewritten_query)
    all_queries = [rewritten_query] + expanded_queries

    # Debug (UI visible)
    with st.expander("🔍 Debug Info"):
        st.write("Original:", query)
        st.write("Rewritten:", rewritten_query)
        st.write("Expanded:", expanded_queries)

    # Step 3: Hybrid Retrieval
    dense_docs, sparse_docs = hybrid_retrieve(
        all_queries,
        vectorstore,
        bm25,
        documents
    )

    # Step 4: Fusion
    fused_docs = rrf_fusion(dense_docs, sparse_docs)

    if not fused_docs:
        st.warning("No relevant documents found.")
        return "I don't know", []

    # Step 5: Re-ranking
    reranked_docs = rerank(query, fused_docs, top_n=MAX_CONTEXT_CHUNKS)

    # Step 6: Compression
    final_docs = compress_documents(reranked_docs)

    # Step 7: LLM
    prompt = build_prompt(query, final_docs)
    answer = generate_answer(prompt)

    return answer, final_docs