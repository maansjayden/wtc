# The price of the coke
amount_due = 50

# accepted coins
coins = [25, 10, 5]

# while loop to keep asking for coins while there us still an amount due
while amount_due > 0:
    print(f"Amount due: {amount_due}")
    coin = int(input("Insert coin: "))

# subtrack coib value from amount due
    if coin in coins:
        amount_due -= coin
# print change and use "abs"to make sure change is positive
print(f"Change owed: {abs(amount_due)}")
