from langchain_community.document_loaders import PyPDFLoader
import tempfile

def load_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        path = tmp.name

    loader = PyPDFLoader(path)
    return loader.load()