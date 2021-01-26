def leapyear():
    # Part One
    # Get the year from participant
    # No error handling
    year = int(input("Enter a year:"))
    #Part Two
    # Check if the year is a leap year
    if year%4 == 0:
        #Part Three
        if year%100 == 0:
            if year%400 == 0:
                print(str(year) + " is a leap year")
            else: print(str(year) + " is not a leap year")
        else: print(str(year) + " is a leap year")
    else: print(str(year) + " is not a leap year")
# Calls leapyear function (Pruush)
leapyear()