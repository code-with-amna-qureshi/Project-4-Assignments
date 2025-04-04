def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    
    for fruit_name, price in fruits.items():
        while True:
            try:
                amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
                if amount_bought < 0:
                    print("Please enter a non-negative number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        total_cost += price * amount_bought

    print(f"Your total is ${total_cost:.2f}")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
