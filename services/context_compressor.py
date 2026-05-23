def compress_documents(documents, max_chars=1000):
    compressed = []

    for doc in documents:
        text = doc.page_content[:max_chars]  # simple truncation
        doc.page_content = text
        compressed.append(doc)

    return compressed