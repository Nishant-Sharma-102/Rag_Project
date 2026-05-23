def multi_query_retrieve(queries, vectorstore, k=5, final_k=5):
    doc_dict = {}

    for q in queries:
        docs = vectorstore.similarity_search(q, k=k)

        for rank, doc in enumerate(docs):
            content = doc.page_content

            # Assign score (higher = better)
            score = 1 / (rank + 1)

            if content in doc_dict:
                doc_dict[content]["score"] += score
            else:
                doc_dict[content] = {
                    "doc": doc,
                    "score": score
                }

    # Sort by score
    sorted_docs = sorted(
        doc_dict.values(),
        key=lambda x: x["score"],
        reverse=True
    )

    # Return top final_k docs
    return [item["doc"] for item in sorted_docs[:final_k]]