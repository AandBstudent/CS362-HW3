def leapyear():
    # Part One
    # Get the year from participant
    # Checks if participant enter a number
    # if not they suck so i'll ask them again
    while True:
        try:
            year = int(input("Enter a year:"))
            break
        except:
            print("Enter a number bruh.")
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