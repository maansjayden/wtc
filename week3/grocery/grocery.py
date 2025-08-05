# Empty List for grocery
groceries = {}

# While loop with try catch for error handeling
while True:
    try:
        # let the user input grocery item and convert to uppercse
        item = input().upper()

        # +1 to item count if already in the list
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

        # this part will run after Ctr + D
    except EOFError:
        for item in sorted(groceries):
            print(groceries[item], item)
        break
