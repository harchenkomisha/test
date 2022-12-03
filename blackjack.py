def ask_yes_no(question):
    """Задает вопрос с ответом(y/n)."""
    response = None 
    while response not in ("y", "n"):
        response = input(question + '(y/n)?').lower()
    return response