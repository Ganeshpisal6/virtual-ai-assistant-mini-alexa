def rule_based_recommendation():
    """Demonstrate a simple rule-based recommendation using time of day."""

    from datetime import datetime

    current_hour = datetime.now().hour

    print("\nAssistant: Rule-Based Recommendation Demo")

    if 5 <= current_hour < 12:
        recommendation = "Good morning! You may enjoy starting your day with learning or exercise."
    elif 12 <= current_hour < 17:
        recommendation = "Good afternoon! You may enjoy focusing on productive work or study."
    elif 17 <= current_hour < 21:
        recommendation = "Good evening! You may enjoy exercise, hobbies, or relaxation."
    else:
        recommendation = "It's nighttime. You may want to relax and prepare for a good night's sleep."

    print(f"Assistant: Recommendation: {recommendation}")


def perceptron_demo():
    """Demonstrate a simple perceptron using an AND-like rule."""

    print("\nAssistant: Simplified Perceptron Demo")
    print("Enter two values: 0 or 1.")

    try:
        x1 = int(input("You: Enter first value (0 or 1): "))
        x2 = int(input("You: Enter second value (0 or 1): "))

        if x1 not in [0, 1] or x2 not in [0, 1]:
            print("Assistant: Please enter only 0 or 1.")
            return

        # Simple perceptron weights and bias
        weight1 = 1
        weight2 = 1
        bias = -1

        # Calculate weighted sum
        total = (x1 * weight1) + (x2 * weight2) + bias

        # Step activation function
        if total >= 1:
            output = 1
        else:
            output = 0

        print(f"Assistant: Perceptron output: {output}")

    except ValueError:
        print("Assistant: Please enter valid numbers: 0 or 1.")
