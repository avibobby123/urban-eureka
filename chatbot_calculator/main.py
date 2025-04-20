from inp import parse_input

def perform_calculation(operation, numbers):
    try:
        numbers = [float(num) for num in numbers]
        if len(numbers) < 2:
            return "Please provide two numbers."

        if operation == "add":
            return numbers[0] + numbers[1]
        elif operation == "subtract":
            return numbers[0] - numbers[1]
        elif operation == "multiply":
            return numbers[0] * numbers[1]
        elif operation == "divide":
            if numbers[1] == 0:
                return "Error: Division by zero"
            return numbers[0] / numbers[1]
        else:
            return "Sorry, I didn't understand the operation."
    except ValueError:
        return "Invalid number input."

def main():
    print("Welcome to Chatbot Calculator!")
    print("Type your question (e.g., 'add 2 and 3') or type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        operation, numbers = parse_input(user_input)
        result = perform_calculation(operation, numbers)
        print("Bot:", result)

if __name__ == "__main__":
    main()