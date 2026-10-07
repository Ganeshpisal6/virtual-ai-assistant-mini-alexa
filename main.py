from greetings import get_user_name, build_greeting
from datetime_utils import get_current_date, get_current_time
from calculator import calculate
from content import get_random_quote, get_random_joke, get_random_fact
from game import play_guessing_game
from ai_concepts import rule_based_recommendation, perceptron_demo


def show_help():
    """Display the commands currently supported by the assistant."""
    print("\nAssistant: Here are the commands I currently understand:")
    print("  - help")
    print("  - date")
    print("  - time")
    print("  - calculate 10 + 5")
    print("  - exit")
    print("  - quit")
    print("  - bye")
    print("  - quote")
    print("  - joke")
    print("  - fact")
    print("  - game")
    print("  - recommend")
    print("  - perceptron")

def main():
    """Start and control the Mini Alexa assistant."""

    user_name = get_user_name()
    print(build_greeting(user_name))

    while True:
        command = input("\nYou: ").strip().lower()

        if command in ["exit", "quit", "bye"]:
            print(f"Assistant: Goodbye, {user_name}! Have a great day.")
            break

        elif command == "help":
            show_help()

        elif command == "date":
            print(f"Assistant: Today's date is {get_current_date()}.")

        elif command == "time":
            print(f"Assistant: The current time is {get_current_time()}.")

        elif command.startswith("calculate "):
            expression = command.replace("calculate ", "", 1)
            print(f"Assistant: {calculate(expression)}")

        elif command == "quote":
            print(f"Assistant: {get_random_quote()}")

        elif command == "joke":
            print(f"Assistant: {get_random_joke()}")

        elif command == "fact":
            print(f"Assistant: {get_random_fact()}")

        elif command == "game":
            play_guessing_game()

        elif command == "recommend":
            rule_based_recommendation()

        elif command == "perceptron":
            perceptron_demo()    

        else:
            print(
                "Assistant: I'm not sure I understood that. "
                "Type 'help' to see what I can do."
            )


if __name__ == "__main__":
    main()