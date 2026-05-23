from rank_bm25 import BM25Okapi

def create_bm25_index(chunks):
    tokenized_docs = [doc.page_content.split() for doc in chunks]

    bm25 = BM25Okapi(tokenized_docs)

    return bm25, chunks