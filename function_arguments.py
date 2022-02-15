# function Arguments and Parameters

# parameters are used when we define a function.
def say_hello(name='rajesh', emoji=':-P'):  # it has default parameters.
    print(f'hello {name} {emoji}')


# arguments are used when we call/invoke a function.
say_hello('mukthy', ':-)')
say_hello('rock', ':-)')

# these are also called positional arguments, because the position of the arguments are important.
say_hello(':-)', 'mukthy')

# keyword arguments, here it does not matter where we place the emoji or name parameters because we actually tell explicity what emoji should be and what name should be.
say_hello(emoji=':-)', name='mukthy')


def say_age(name='rajesh', age='26'):  # it has default parameters.
    print(f'hello your name is {name} and age is {age}')


say_age('mukthy', '29')
say_age('rock', '24')

# when function does not have any arguments or only one argments then it will take the predefined value (default parameters) from the function definition.

say_age('timmy')
say_age()

# Default parameters are defined in the function definition.
# Keyword arguments are defined in the function call.
