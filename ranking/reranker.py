from sentence_transformers import CrossEncoder

# Load once (IMPORTANT)
model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")

def rerank(query, documents, top_n=5):
    pairs = [(query, doc.page_content) for doc in documents]

    scores = model.predict(pairs)

    scored_docs = list(zip(documents, scores))

    ranked_docs = sorted(
        scored_docs,
        key=lambda x: x[1],
        reverse=True
    )

    return [doc for doc, _ in ranked_docs[:top_n]]