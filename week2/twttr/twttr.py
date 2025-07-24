# Get the input text from the user
input = input("input: ")

# convert to lowercase and  Look for all the vowels in the user input
for char in input:
    if char.lower() in ["a", "e" , "i" , "o" , "u"]:
        # Remove the vowels by replacing it with nothing
        input = input.replace(char, "")

# print the output
print("Output: ", input)
