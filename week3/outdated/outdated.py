def main():
    # ask user to input date, capitilize word.
    date = input("Date: ").strip().title()
    find(date)

# list of monts used for validation
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def find(date):
    while True:
        try:
            # Try to handle the MM/DD/YYYY format.
            # The 'ValueError' from split() to handle bad formats.
            mm, dd, yyyy = date.split("/")
            mm = int(mm)
            dd = int(dd)

            # check to see if the month and day are correct
            if(mm < 12 and dd < 32):
                print(f"{yyyy}-{mm:02}-{dd:02}")
                break
            else:
                # If the check fails, restart program.
                main()

        # If a ValueError occurs, try the next format
        except ValueError:
            # Check for the "Month Day, Year" format
            if(", " in date and date[0:2].isalpha()):
                month, year = date.split(", ")
                month, day = month.split(" ")
                day = int(day)
                if(month in months and day<32):
                    print(f"{year}-{months.index(month)+1:02}-{day:02}")
                else:
                    main()
            else:
                main()
        break
main()
