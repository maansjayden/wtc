def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if it's between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Cgeck if the first two char is letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Check if All characters are alphanumeric
    if not s.isalnum():
        return False

    number_started = False  # check if we've started reading digits
    for char in s:
        if char.isdigit():
            if not number_started:
                if char == '0':
                    return False  # No leading zero allowed
                number_started = True
        elif number_started:
            return False  # No letters allowed after a number starts

    return True


main()
