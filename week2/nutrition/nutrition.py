# Let the user input the fruit, convert it to lower and strip whitespace
fruit = input("Enter a fruit: ").lower().strip()

# Dictionary to store fruit names with the value of their calories
fruits = { "apple": "130",
"avocado": "50",
"banana": "110",
"cantaloupe": "50",
"grapefruit": "60",
"grapes": "90",
"honeydew melon": "50",
"kiwifruit": "90",
"lemon": "15",
"lime": "20",
"nectarine": "50",
"orange": "80",
"peach": "60",
"pear": "100",
"pineapple": "50",
"plums": "70",
"strawberries": "50",
"sweet cherries": "100",
"tangerine": "50",
"watermelon": "80"}

# Check if the fruit that the usre has inserted, is in the dictionary and print calories
if fruit in fruits:
    print(f"Calories: {fruits[fruit]} ")
