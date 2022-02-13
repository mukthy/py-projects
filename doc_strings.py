# DocStrings used to provide comments or inforamtion.

def test(a):
    '''
    Info: This function takes a as argument and prints the value for a
    '''
    print(a)


test('@!@')
# this will give us an output of the docstrings just like a documentations just like a man command.
print(help(test))
print(test.__doc__)  # this will print the docstring on the terimnal.
