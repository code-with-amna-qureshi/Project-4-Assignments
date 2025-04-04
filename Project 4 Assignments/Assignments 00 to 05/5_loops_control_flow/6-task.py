def main():
    curr_value = int(input("Enter a number: "))  # Get user input
    
    while curr_value < 100:
        print(curr_value, end=" ")  # Print the current value
        curr_value *= 2  # Double the value
    
    print(curr_value)  # Print the final value which is 100 or more


# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()
