#input
x,y,z = input("Expression: ").strip().split()

# convert values to floats
x = float(x)
z = float(z)

#Check opperator and do calculation
if y == "+":
    print(x + z)
elif y == "-":
    print (x - z)
elif y == "*":
    print (x * z)
elif y == "/":
    print (x / z)
