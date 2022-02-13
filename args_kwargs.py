# *args ==> Arguments
# **kwargs ==> Keyword Arguments.

# *args in a function definition can take any number of arguments.
# *kwargs in a function definition can take any number of key word arguments.

# if we print(args) it will give us a tuple of items of the arguments that we pass.
# if we print(kwargs) it will give us a dict of tiems of the arguments that we pass.

def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0
    for items in kwargs.values():
        total = total + items

    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=10, num2=5))

# order of arguments or parameters.

# RULE:  parameters, *args, default arguments, **kwargs

print("With RULE applied")


def super_func2(name, *args, age=30, **kwargs):
    print(name, args)
    print(age, kwargs)
    total = 0
    for items in kwargs.values():
        total = total + items

    return sum(args) + total


print(super_func2('Mukthy', 1, 2, 3, 4, 5, age=29, num1=10, num2=5))
