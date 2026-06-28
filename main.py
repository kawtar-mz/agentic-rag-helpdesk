from dotenv import load_dotenv
load_dotenv()

from src.loader import load_documents
from src.splitter import split_documents
from src.vectorstore import create_vectorstore, get_retriever

# 1. Charger
documents = load_documents()

# 2. Découper
chunks = split_documents(documents)

# 3. Vectoriser
vectorstore = create_vectorstore(chunks)

# 4. Retriever
retriever = get_retriever(vectorstore)

# Test
query = "Mon ordinateur est lent"
results = retriever.invoke(query)

print("\nRésultats :")
for doc in results:
    print("-", doc.page_content)