import random
import sys


def run_guess(choice, r):
    try:

        if 0 < choice < 4:
            if r == choice:
                print(f'You are a genius, you choice matched with random number {r}')
                return True

            else:
                print(f'Trying Again, since the random generated number {r} does not match your choice {choice}')
                return False

        else:
            print('Enter a number between 1-3')
            return False

    except TypeError:
        print('please enter a number')
        return False


if __name__ == '__main__':
    r = random.randint(1, 3)
    while True:

        try:
            choice = int(input('Enter a number between 1 and 3 \n'))
            if run_guess(choice, r):
                break
        except ValueError:
            print('please enter a number')
            continue
