#Get user input and convert to string
user = str(input("What answer to the Great Question of Life, the Universe and Everything?"))

#Convert user input to lower-Case and remove whitespace
user = user.lower().strip()

#Check the users input
if user == "42" or user == "forty-two" or user == "forty two":
    print("Yes")
else:
    print ("No")
