from retrieval.dense_retriever import multi_query_retrieve
from retrieval.sparse_retriever import bm25_retrieve


def hybrid_retrieve(queries, vectorstore, bm25, documents, k=5):
    # Dense retrieval
    dense_docs = multi_query_retrieve(queries, vectorstore, k=k, final_k=k)

    # Sparse retrieval (use first query only for simplicity)
    sparse_docs = bm25_retrieve(queries[0], bm25, documents, k=k)

    return dense_docs, sparse_docs