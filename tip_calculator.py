# To calculate the tip for hotel.
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percent_of_tip = float(
    input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))

percent = percent_of_tip/100

tip = total_bill * percent

total = total_bill + tip

per_person = total / number_of_people

#round_off = round(per_person, 2)
round_off = "{:.2f}".format(per_person)
print(f"Each person should pay: ${round_off}")
