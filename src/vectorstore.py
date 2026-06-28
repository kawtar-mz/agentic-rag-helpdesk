from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import FAISS
from sklearn.feature_extraction.text import TfidfVectorizer

class TfidfEmbeddings(Embeddings):
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.fitted = False

    def embed_documents(self, texts):
        if not self.fitted:
            vectors = self.vectorizer.fit_transform(texts)
            self.fitted = True
        else:
            vectors = self.vectorizer.transform(texts)
        return vectors.toarray().tolist()

    def embed_query(self, text):
        vector = self.vectorizer.transform([text])
        return vector.toarray()[0].tolist()


def create_vectorstore(chunks):
    texts = [doc.page_content for doc in chunks]

    embeddings = TfidfEmbeddings()

    vectorstore = FAISS.from_texts(
        texts,
        embedding=embeddings
    )

    return vectorstore


def get_retriever(vectorstore):
    return vectorstore.as_retriever()