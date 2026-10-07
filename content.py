import random


QUOTES = [
    "Believe you can and you're halfway there.",
    "Success is the sum of small efforts repeated every day.",
    "Don't watch the clock; do what it does. Keep going.",
    "The future depends on what you do today.",
    "Great things take time. Keep working."
]


JOKES = [
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why was the computer cold? It left its Windows open!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the smartphone need glasses? Because it lost its contacts!"
]


FACTS = [
    "The Earth takes about 365 days to orbit the Sun.",
    "Water covers about 71 percent of Earth's surface.",
    "Honey can remain preserved for a very long time when stored properly.",
    "The human brain uses a significant amount of the body's energy."
]


def get_random_quote():
    """Return a random motivational quote."""
    return random.choice(QUOTES)


def get_random_joke():
    """Return a random joke."""
    return random.choice(JOKES)


def get_random_fact():
    """Return a random interesting fact."""
    return random.choice(FACTS)