import random


def play_guessing_game():
    """Run a simple number guessing game."""

    secret_number = random.randint(1, 20)
    max_attempts = 5
    attempts = 0

    print("\nAssistant: I'm thinking of a number between 1 and 20.")
    print(f"Assistant: You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("You: "))
            attempts += 1

            if guess < secret_number:
                print("Assistant: Higher!")

            elif guess > secret_number:
                print("Assistant: Lower!")

            else:
                print(
                    f"Assistant: Correct! You guessed it in "
                    f"{attempts} attempt(s)."
                )
                return

        except ValueError:
            print("Assistant: Please enter a whole number.")

    print(
        f"Assistant: Game over! The number was {secret_number}."
    )