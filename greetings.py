def get_user_name():
    """Ask the user for their name and return it."""
    name = input("Assistant: Hi! I'm Mini Alexa. What's your name?\nYou: ")
    return name.strip()


def build_greeting(name):
    """Create a welcome message using the user's name."""
    return f"Assistant: Nice to meet you, {name}! Type 'help' to see what I can do."