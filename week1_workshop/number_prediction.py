import random

secret_number = random.randint(1, 10)
"""The secret number the user needs to guess (between 1 and 10)."""

def main():
    """
    Main function to run the number guessing game.
    Keeps asking the user to guess until they get it right.
    """

    while True:
        try:
            user_input = input("Enter your guess from 1-10: ").strip()

            # Condition 1 — Empty input
            if user_input == "":
                print("Input cannot be empty! Please enter a number.")
                continue

            # Condition 2 — Decimal/float input
            if "." in user_input:
                print("Please enter a whole number only, no decimals!")
                continue

            guess = int(user_input)

            # Condition 3 — Out of range
            if guess < 1 or guess > 10:
                print("Number must be between 1 and 10 only!")
                continue

            # Main game logic
            if guess > secret_number:
                print("Too High!")
            elif guess < secret_number:
                print("Too Low!")
            else:
                print("Congratulations! You guessed it right.")
                print(f"The secret number was {secret_number}")
                break

        except ValueError:
            # Condition 4 — Letters or symbols
            print("Invalid input! Please enter a number only.")


if __name__ == "__main__":
    main()