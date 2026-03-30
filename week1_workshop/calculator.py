def get_numbers():
    """Prompt the user to enter two numbers."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input! Please enter numeric values only.\n")


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return None  
    return num1 / num2


def display_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 35)
    print("       SIMPLE CALCULATOR MENU")
    print("=" * 35)
    print("  1. Addition       ( + )")
    print("  2. Subtraction    ( - )")
    print("  3. Multiplication ( * )")
    print("  4. Division       ( / )")
    print("  5. Exit")
    print("=" * 35)


def main():
    """Main function to control the calculator workflow."""
    print("\nWelcome to the Simple Calculator!")

    while True:
        display_menu()

        choice = input("Select an operation (1-5): ").strip()

        # Exit condition
        if choice == "5":
            print("\nThank you for using the calculator. Goodbye!")
            break

        # Validate menu choice
        if choice not in ("1", "2", "3", "4"):
            print("Invalid selection! Please choose a number between 1 and 5.\n")
            continue

        # Get two numbers from the user
        num1, num2 = get_numbers()

        # Perform the selected operation
        if choice == "1":
            result = add(num1, num2)
            print(f"\n Result: {num1} + {num2} = {result}")

        elif choice == "2":
            result = subtract(num1, num2)
            print(f"\n Result: {num1} - {num2} = {result}")

        elif choice == "3":
            result = multiply(num1, num2)
            print(f"\n Result: {num1} * {num2} = {result}")

        elif choice == "4":
            result = divide(num1, num2)
            if result is None:
                print("\n Error: Division by zero is not allowed!")
            else:
                print(f"\n Result: {num1} ÷ {num2} = {result}")


if __name__ == "__main__":
    main()