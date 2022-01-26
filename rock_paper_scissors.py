import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
choice = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

if choice >= 0 or choice < 3:
    print("Invalid Selection of choice, Please select between 0 to 2")
else:
    print(game_images[choice])

# print(choice)
computer = random.randint(0, 2)

# Rock wins against Scissors
if choice == '0':
    print(rock)
    if computer == 0:
        print("Computer Choose: \n")
        print(rock)
        print("Draw")
    elif computer == 1:
        print("Computer Choose: \n")
        print(paper)
        print("You loose")
    else:
        print("Computer Choose: \n")
        print(scissors)
        print("You won")

# Paper wins against rock
elif choice == '1':
    print(paper)
    if computer == 0:
        print("Computer Choose: \n")
        print(rock)
        print("You won")
    elif computer == 1:
        print("Computer Choose: \n")
        print(paper)
        print("You draw")
    else:
        print("Computer Choose: \n")
        print(scissors)
        print("You lose")

# Scissors win against paper
elif choice == '2':
    print(scissors)
    if computer == 0:
        print("Computer Choose: \n")
        print(rock)
        print("You lose")
    elif computer == 1:
        print("Computer Choose: \n")
        print(paper)
        print("You won")
    else:
        print("Computer Choose: \n")
        print(scissors)
        print("You draw")
else:
    print("You entered wrong choice!!")
