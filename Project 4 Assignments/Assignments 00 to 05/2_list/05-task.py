
def get_first_element(lst):
    """
    Prints the first element of a provided list, if available.
    """
    if lst:  # Check if the list is not empty
        print("First element:", lst[0])
    else:
        print("The list is empty. No first element to display.")

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")
        if elem == "":  # Stop when the user presses enter
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()
