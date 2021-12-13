
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names)
payee = random.randint(0, length-1)
print(f"{names[payee]} is going to buy the meal today!")
