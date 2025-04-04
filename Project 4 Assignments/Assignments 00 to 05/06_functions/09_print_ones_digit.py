def print_ones_digit(num):
    ones_digit = num % 10  # Get the ones digit
    print(f"The ones digit is {ones_digit}")


def main():
    num = int(input("Enter a number: "))  # Get user input
    print_ones_digit(num)  # Call the function


# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()
