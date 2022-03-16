import random
import sys

start = int(sys.argv[1])
last = int(sys.argv[2])

while True:
    r = random.randint(start, last)
    choice = int(input('Enter a number between 1 and 3 \n'))

    if r == choice:
        print(f'You are a genius, you choice matched with random number {r}')
        break

    else:
        print(f'Trying Again, since the random generated number {r} does not match your choice {choice}')
