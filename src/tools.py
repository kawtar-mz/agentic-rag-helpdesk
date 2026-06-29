# Tool 1 : recherche documentaire
def search_tool(retriever, question):
    results = retriever.invoke(question)
    return [doc.page_content for doc in results]


# Tool 2 : diagnostic simple
def diagnostic_tool(question):
    question = question.lower()

    if "lent" in question:
        return "Votre ordinateur semble lent. Essayez de fermer les applications inutiles et redémarrer votre appareil."
    
    elif "wifi" in question or "internet" in question:
        return "Vérifiez votre connexion Wi-Fi, redémarrez votre routeur et rapprochez-vous du signal."
    
    elif "mot de passe" in question:
        return "Utilisez la fonction 'mot de passe oublié' pour réinitialiser votre mot de passe."
    
    elif "ne démarre pas" in question:
        return "Vérifiez l'alimentation et assurez-vous que votre appareil est correctement branché."

    else:
        return "Problème non reconnu. Veuillez consulter le support technique."