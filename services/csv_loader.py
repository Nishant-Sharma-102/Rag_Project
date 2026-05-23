import pandas as pd
from langchain_core.documents import Document
def load_csv(uploaded_file):
    df = pd.read_csv(uploaded_file)

    docs = []
    for _, row in df.iterrows():
        content = " | ".join([f"{col}: {row[col]}" for col in df.columns])
        docs.append(Document(page_content=content))

    return docs