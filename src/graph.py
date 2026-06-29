from langgraph.graph import StateGraph

# État simple
class AgentState(dict):
    pass

retriever_global = None

# NODE : logique principale
def agent_node(state):
    from src.tools import diagnostic_tool, search_tool
    global retriever_global

    question = state.get("question", "").lower()

    # SI diagnostic
    if "lent" in question or "wifi" in question:
        answer = diagnostic_tool(question)
        return {"final_answer": answer}

    # SINON RAG classique
    docs = search_tool(retriever_global, question)

    if not docs:
        return {"final_answer": "Aucune information trouvée."}

    response = "Réponse basée sur les documents :\n"

    for doc in docs[:2]:
        response += f"- {doc}\n"

    return {"final_answer": response}


# Création graphe
def create_graph(retriever):
    global retriever_global
    retriever_global = retriever

    graph = StateGraph(AgentState)

    graph.add_node("agent", agent_node)

    graph.set_entry_point("agent")
    graph.set_finish_point("agent")

    return graph.compile()