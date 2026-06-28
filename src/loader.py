from langchain_community.document_loaders import TextLoader

def load_documents(file_path="data/helpdesk.txt"):
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    return documents