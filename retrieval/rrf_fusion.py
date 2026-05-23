def rrf_fusion(dense_docs, sparse_docs, k=60):
    doc_scores = {}

    # Dense ranking
    for rank, doc in enumerate(dense_docs):
        content = doc.page_content
        score = 1 / (k + rank)

        doc_scores[content] = doc_scores.get(content, 0) + score

    # Sparse ranking
    for rank, doc in enumerate(sparse_docs):
        content = doc.page_content
        score = 1 / (k + rank)

        doc_scores[content] = doc_scores.get(content, 0) + score

    # Sort
    sorted_docs = sorted(
        doc_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for content, _ in sorted_docs for doc in dense_docs + sparse_docs if doc.page_content == content][:5]