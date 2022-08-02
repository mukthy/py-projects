# Type Checking in Python
# https://realpython.com/python-type-checking/
# Dynamic Typing and Static Typing
# Static Typing: The checks are performed without running the program. In most statically typed languages, the checks are performed at compile time.
# The type of variable is not allowed to change over its lifetime. Mechanisms for casting variable to a different type may exist.

# Dynamic Typing: Python is a dynamically typed language. Type hints and type checking are possible.
# PEP484 introduced type hints.
# Other tools exist to static type check using those hints

# Duck Typing: Python supports duck typing.
# The type of class of an object is less important than the method it defines.
# Instead of checking for the class or type, check the object for the presence of specific methods and/or attributes.

class TheHobbit:
    def __len__(self):
        return 95022


the_hobbit = TheHobbit()
print(len(the_hobbit))

a = 'hello'
print(len(a))
