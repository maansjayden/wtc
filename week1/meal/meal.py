def main():
    # Convert time string into Decimal
    time = convert(input("What is the current time? "))

    # Check if the time inserted falls within certai meal times.
    if 7.0 <= time <= 8.0:
        print("Breakfast Time")
    elif 12.0 <= time <= 13.0:
        print("Lunch Time")
    elif 18.0 <= time <= 19.0:
        print("Dinner Time")

def convert(time):
    # Split time into hours and mins
    hr, min = time.split(":")
    # convert hours and minutes into floats, returns time into dec hours
    return float(hr) + float(min)/60


if __name__ == "__main__":
    main()
