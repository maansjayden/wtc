def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # strip / remove dollar sign and return a float
    d=d.strip("$")
    return float(d)


def percent_to_float(p):
     # strip / remove % sign and return a float
     # devide p by 100 to get eg. 0.15
    p = p.strip("%")
    p = int(p) / 100
    return float(p)

main()
