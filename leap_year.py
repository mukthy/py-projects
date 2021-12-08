# to find a year is a leap year or not?
year = int(input("Which year do you want to check? \n"))

four = year % 4

hundred = year % 100

four_hundred = year % 400

if four == 0:
    if hundred == 0:
        if four_hundred == 0:
            print("Leap Year.\n")
        else:
            print("Not leap year.\n")
    else:
        print("Leap Year.\n")
else:
    print("Not leap year.\n")
