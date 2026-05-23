def bm25_retrieve(query, bm25, documents, k=5):
    tokenized_query = query.split()

    scores = bm25.get_scores(tokenized_query)

    # Rank documents
    ranked_docs = sorted(
        list(zip(documents, scores)),
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for doc, _ in ranked_docs[:k]]