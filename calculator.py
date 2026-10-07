def calculate(expression):
    """Perform basic arithmetic on a simple expression."""

    try:
        expression = expression.replace("+", " + ")
        expression = expression.replace("-", " - ")
        expression = expression.replace("*", " * ")
        expression = expression.replace("/", " / ")

        parts = expression.split()

        if len(parts) != 3:
            return "Please use the format: number operator number"

        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":
            if num2 == 0:
                return "Cannot divide by zero."
            result = num1 / num2

        else:
            return "Unsupported operator. Use +, -, * or /."

        return f"Result: {result}"

    except ValueError:
        return "Please enter valid numbers."


def calculator_help():
    """Explain how to use the calculator."""
    return "Example: calculate 10 + 5"  