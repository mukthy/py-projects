# it usually have @ symbol at the start. It is possible because these functions acts as variables.

# Higer Order Function is A function which accepts another function as a parameter or returns a function is a higher order function.

def great(func):
    func()


def greet2():
    def func():
        return 5
    return func


# filter(), map() are also decorators

# Decorator is A function that wraps another function and enhaces it or changes it.


def my_decorator(func):
    def wrap_func():
        print('*********')
        func()
        print('*********')
    return wrap_func


my_decorator


def hello():
    print('hellloooo')


@my_decorator
def bye():
    print('See ya later')

# decorator can be defined like below as well. this is how decorator works under the hood.


a = my_decorator(hello)
a()
my_decorator(hello)()
hello()
bye()
