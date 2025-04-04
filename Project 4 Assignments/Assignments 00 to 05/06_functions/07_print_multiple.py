def main():
    message = input("Please type a message: ")  # Get user message
    times = int(input("Enter a number of times to repeat your message: "))  # Get repeat count
    
    for _ in range(times):
        print(message, end=" ")  # Print message multiple times
    print()


# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()
