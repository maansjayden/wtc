#Check user input
greeting = input("Greeting: ")
greeting = greeting.lower().strip()

# Check if input has a "hello", print $0
if greeting.startswith("hello"):
    print("$0")

#Check of input has "H", print $20
elif greeting[0] == "h" :
    print("$20")

#otherwise print #100
else: print("$100")

