#get user input for a camel case word
word = input("Enter a camel case word: ")

# Initialise an empty string for snake_case
snake_case = ""

# Convert camel case to snake case
# Iterate through each character in the input word
for char in word:
    # If the character is uppercase, add an underscore before it
    if char.isupper():
        # Avoid adding a "_" at the start
        if snake_case:
            snake_case += "_"
        # Convert uppercase letter to lowercase a
        snake_case += char.lower()
    # If the character is lowercase, just add it to the snake_case string
    else:
        snake_case += char
print("Snake case:", snake_case)

