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


# Type Hinting
# Annotate the arguments and the return value of a function with a type hint.

def greet(name: str) -> str:
    return f'Hello, {name}!'


# The name: str syntax indicates the name argument should be of type str.
# The -> syntax indicates the return value should be of type str.

def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()}".center(50, "o")


print(headline('123', align=True))

# PEP8 Recommendations
# Use normal rules for colons, no space before and one space after a colon.

text: str

# Use spaces around the = sign when combining an argument annotation with a default value.

align: bool = True


# Use spaces around the -> arrow.

# def headline2(...) -> str:
#     pass

# Type Checking with Mypy
# Mypy is a Python type checker. It combines the expressive power and convenience of python with a powerful type system and compile-time type checking.
# Initially started as a standalone variant of python with seamless dynamic and static typing.
# Was rewritten to use annotations making it a static type check for regular python code.
def headline2(text: str, centered: bool = False) -> str:
    if not centered:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


print(headline2.__annotations__)
print(headline2('123', centered=True))


# type comments

def func(arg):
    # type: (float) -> float
    age = 42  # type: int
    return age * arg


print(func(2.0))


def headline3(text3, width=80, centered3=False):
    # type: (str, int, bool) -> str
    if not centered3:
        return f"{text3.title()}\n{'-' * len(text3)}"
    else:
        return f" {text3.title()} ".center(50, "o")


# Example of python types using list, dict and tuple

from typing import List, Dict, Tuple

names: List[str] = ['John', 'Paul', 'George', 'Ringo']
version: Tuple[int, int, int] = (1, 2, 3)
options: Dict[str, bool] = {'bold': True, 'hidden': False}

print(__annotations__)
