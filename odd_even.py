# find odd or even
number = int(input("Which number do you want to check? "))
result = number % 2

if result == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")
