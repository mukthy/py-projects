# it usually have @ symbol at the start. It is possible because these functions acts as variables.

# A function which accepts another function as a parameter or returns a function is a higher order function.

def great(func):
    func()


def greet2():
    def func():
        return 5
    return func
# filter(), map() are also decorators
