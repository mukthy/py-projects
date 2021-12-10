print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

couple = name1.lower() + name2.lower()

true = str(couple.count('t') + couple.count('r') +
           couple.count('u') + couple.count('e'))

love = str(couple.count('l') + couple.count('o') +
           couple.count('v') + couple.count('e'))

score = int(true+love)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
