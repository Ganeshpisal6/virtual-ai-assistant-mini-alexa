def rule_based_recommendation():
    """Demonstrate a simple rule-based recommendation system."""

    print("\nAssistant: Rule-Based Recommendation Demo")
    print("Answer the following questions.")

    interest = input("You: What do you like - technology, sports, or music? ").strip().lower()

    if interest == "technology":
        recommendation = "You may enjoy learning Python and Artificial Intelligence."

    elif interest == "sports":
        recommendation = "You may enjoy exploring sports analytics."

    elif interest == "music":
        recommendation = "You may enjoy learning about music technology."

    else:
        recommendation = "Try exploring different topics to discover your interests."

    print(f"Assistant: Recommendation: {recommendation}")


def perceptron_demo():
    """Demonstrate a very simple perceptron for an AND-like rule."""

    print("\nAssistant: Simplified Perceptron Demo")
    print("Enter two values: 0 or 1.")

    try:
        x1 = int(input("You: Enter first value (0 or 1): "))
        x2 = int(input("You: Enter second value (0 or 1): "))

        if x1 not in [0, 1] or x2 not in [0, 1]:
            print("Assistant: Please enter only 0 or 1.")
            return

        # Simple weights and bias.
        weight1 = 1
        weight2 = 1
        bias = -1

        # Weighted sum.
        total = (x1 * weight1) + (x2 * weight2) + bias

        # Step activation function.
        if total >= 1:
            output = 1
        else:
            output = 0

        print(f"Assistant: Perceptron output: {output}")

    except ValueError:
        print("Assistant: Please enter valid numbers: 0 or 1.")