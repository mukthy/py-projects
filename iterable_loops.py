from traceback import print_tb


user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
for item in user.items():  # prints the key:value pairs in a tuple format.
    print(item)
for item in user.values():  # prints only the values of the keys.
    print(item)
for item in user.keys():  # prints only the keys of the dictionary.
    print(item)

for key, value in user.items():  # to return the key:value pairs without a tuple format
    print(key, value)
