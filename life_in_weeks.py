# Print the life that you have left in days, weeks and months.
age = input("What is your current age?\n")

left = 90 - int(age)  # left age in years
# print(left)
days = left * 365  # left age in days
weeks = left * 52  # left age in weeks
months = left * 12  # left age in months

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
