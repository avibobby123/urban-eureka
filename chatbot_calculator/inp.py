import spacy
nlp = spacy.load("en_core_web_sm")

def parse_input(user_input):
    doc = nlp(user_input.lower())
    numbers = [token.text for token in doc if token.like_num]
    if "add" in user_input or "plus" in user_input:
        return "add", numbers
    elif "subtract" in user_input or "minus" in user_input:
        return "subtract", numbers
    elif "multiply" in user_input or "times" in user_input:
        return "multiply", numbers
    elif "divide" in user_input or "over" in user_input:
        return "divide", numbers
    else:
        return "unknown", numbers