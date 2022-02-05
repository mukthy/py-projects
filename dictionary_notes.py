# Dictionary
# Dictionary can have a key which are immutable.
dictionary = {
    'a': 1,
    'b': 2
}
print(dictionary['b'])

# in disctionary we can give the list of items as a value for a key a string as a value and even a Boolean also.
dictionary = {
    'a': [1, 2, 3],
    'b': 'hello',
    'x': True
}
# if we want to access an item in a list, and the list is a value for a key then we have to do like this.
print(dictionary['a'][1])

li = [
    {
        'a': [1, 2, 3],
        'b': 'hello',
        'x': True
    },
    {
        'a': [4, 5, 6],
        'b': 'hello',
        'x': True
    }
]
print(li[0]['a'][2])


# Dictonary Methods

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'mage': 30
}

# this get() dictionary method can be used to see if a key is present in the dictionary.
print(user.get('age'))

# it can be used print 55 when the key age is not present in the dictionary.
print(user.get('age', 55))

# Not a common way to create a dictionary.
user2 = dict(fname='nathan', lname='M')
print(user2)

# to check if a key is present in the Dictionary:

print('basket' in user)

# to check if a key is present in the dictionary using .key() method

print('greet' in user.keys())

# to check if a value is present in the dictionary using .key() method
print('hello' in user.values())

# this will return the items in the dictionary and it will show/return the key:value pairs as a tuple.
print(user.items())


# to clear or removes the items from the dictionary.
# user.clear()
print(user)

# to copy the entire dictionary to another dictionary variable

user2 = user.copy()
print(user2)

# to remove or pop an value from the dictionary.

# print(user2.pop('mage'))
print(user2)

# to remove the last key:value pair which was inserted into the dictionary.

# print(user2.popitem())
# print(user2.popitem())

# print(user2)

# to update an value for a key or to update/add a key:value pair to the dictionary
print(user2.update({"age": 55}))
print(user2.update({"mage": 35}))
print(user2)
