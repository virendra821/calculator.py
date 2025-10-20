def add(n1: float, n2: float) -> float:
    return n1 + n2

def subtract(n1: float, n2: float) -> float:
    return n1 - n2

def multiply(n1: float, n2: float) -> float:
    return n1 * n2

def divide(n1: float, n2: float) -> str | float:
    if n2 == 0:
        return "ERROR: Division by zero"
    return n1 / n2

def get_number_input(prompt: str) -> float | None:
    while True:
        try:
            user_input = input(prompt).strip()
            if user_input.lower() == 'q':
                return None
            return float(user_input)
        except ValueError:
            print("Invalid numeric input.")

def calculator_cli():
    print("CLI Calculator Initialized.")
    print("Type 'q' to quit.")

    while True:
        print("\n--- Menu ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit (q)")
        
        choice = input("Enter choice (1-5 or q): ").strip()

        if choice == '5' or choice.lower() == 'q':
            print("Exiting calculator.")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = get_number_input("Enter first number: ")
            if num1 is None: continue

            num2 = get_number_input("Enter second number: ")
            if num2 is None: continue

            result = None
            operation_symbol = ""

            match choice:
                case '1':
                    result = add(num1, num2)
                    operation_symbol = "+"
                case '2':
                    result = subtract(num1, num2)
                    operation_symbol = "-"
                case '3':
                    result = multiply(num1, num2)
                    operation_symbol = "*"
                case '4':
                    result = divide(num1, num2)
                    operation_symbol = "/"

            if isinstance(result, str):
                print(f"{result}")
            else:
                print(f"Result: {num1} {operation_symbol} {num2} = {result}")
        else:
            print("Invalid choice. Select 1-5 or q.")

calculator_cli()
