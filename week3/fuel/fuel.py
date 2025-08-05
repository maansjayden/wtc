while True:
    fuel = input("Fractional fuel: ")
    try:
        x, y = fuel.split('/')
        x = int(x)
        y = int(y)

        if x > y or x < 0 or y <= 0:

            continue  # Invalid fraction, ask again

        output = (x / y) * 100
    except (ValueError, ZeroDivisionError):
        continue  # Bad input or divide by zero, ask again
    else:
        break  # Valid input, break out of the loop

# Show the fuel level
if output <= 1:
    print("E")  # Empty
elif output >= 99:
    print("F")  # Full
else:
    print(f"{round(output)}%")
