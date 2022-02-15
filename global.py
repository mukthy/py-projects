# using Global Keyword
a = 0


def count():
    global a  # to access the global variable a we can use the global keyword.
    a = a + 1
    return a


print(count())

# an alternate way to access the global variables are  passing the parameter and arguments in the funtion itself.:

a = 5


def count(a):  # passing the a as paramenter in the function definition to access the global variable
    a = a + 1
    return a


# passing the a as positional argument.
print(count(a))
