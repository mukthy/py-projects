# scope and its rules.

# Scope - It simply means what variable do I have access to?

global_variable = 100
if True:
    x = 10
    # print(total) # this total variable is not accessible from here, because we are accessing this variable outside of the function.

#global_variable = 100


def some_fun():
    total = 101
    print(total)
    print(x)
    print(global_variable)


print(some_fun())


# Rules of Scope
# 1 - Start with Local check
# 2 - Check the parent local
# 3 - Check the Global Scope
# 4 - built-in python functions.

a = 1  # Global Scope


def parent():
    a = 5  # parent scope

    def confusion():
        # a = 5      #local scope
        return sum  # built - in Python Functions
    return confusion()


print(a)
print(parent())
