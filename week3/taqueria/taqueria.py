# A dictionary to store food item prices
foods = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# A variable to keep track of the total and  = 0
price = 0

# A loop to ask for food items
while True:
    # We use a try-except block to handle potential errors from user input
    try:
        # Prompt the user to enter an item and capitalizes the first letter of a word, strip white space

        user_input = input("Item: ").title().strip()
        # Add the price of the entered item to the running total
        price = price + foods[user_input]
        # Print the current total and concert to two decimal places
        print(f"Total: ${price:.2f}")
    # CTRL+D (EOFError) then this block will execute
    except EOFError:
        # Print a blank line
        print()
        break
    # If the user enters an item that isn't in the dictionary, this block will execute
    except KeyError:
        pass
