def main():
    user_input = ""  # Initialize user_input to an empty string

    while True:
        user_input = input("Tell me a joke! (or type 'exit' to quit): ")  # Get user input
        user_input = user_input.strip().lower()  # Ensure user_input is processed safely

        if user_input == "exit":
            print("Goodbye!")
            break

        print("Here's a joke for you!")  # Replace with actual joke logic

main()
