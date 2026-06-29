from src.loader import load_documents
from src.splitter import split_documents
from src.vectorstore import create_vectorstore, get_retriever
from src.tools import search_tool, diagnostic_tool

# ✅ 1. Charger les documents
documents = load_documents()

# ✅ 2. Découper les documents (chunking)
chunks = split_documents(documents)

# ✅ 3. Créer la base vectorielle
vectorstore = create_vectorstore(chunks)

# ✅ 4. Créer le retriever
retriever = get_retriever(vectorstore)

print("✅ Agent Helpdesk AI prêt !")

# ✅ 5. Mode interactif
while True:
    query = input("\n💬 Pose ta question (ou tape 'exit') : ")

    if query.lower() == "exit":
        print("👋 Au revoir !")
        break

    print("\n🤖 Réponse :")

    # ✅ LOGIQUE AGENT (Agentic RAG)
    if "lent" in query.lower() or "wifi" in query.lower():
        # 👉 diagnostic intelligent
        response = diagnostic_tool(query)

    else:
        # 👉 recherche dans documents (RAG)
        docs = search_tool(retriever, query)

        if not docs:
            response = "❌ Aucune information trouvée."
        else:
            response = docs[0]

    print(response)