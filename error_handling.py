# error handling:
# Error handling helps the program to keep running even after it throws an error.
from decimal import DivisionByZero


while True:
    try:
        age = int(input('Enter your age?'))
        print(10/age)
    except ValueError:
        print('enter a number')
    except ZeroDivisionError:
        print('Please enter a number greater than 0')
    else:
        print('Thank you')
        break


def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as error:
        print(f'Please enter numbers: {error}')


print(sum(1, 2))


def devide(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as error:
        print(f'Please enter numbers: {error}')


print(devide('1', 2))


while True:
    try:
        age = int(input('Enter your age?'))
        print(10/age)
        raise ValueError('hey cut it out')
    # except ValueError:
    #     print('enter a number')
    except ZeroDivisionError:
        print('Please enter a number greater than 0')
    else:
        print('Thank you')
        break
    finally:        # this finally will be used to print or execute that part of code no matter what the while is doing. Even after the Break the finally will be executed.
        print('Ok, I am finally done')
