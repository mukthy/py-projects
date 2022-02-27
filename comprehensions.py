# they are quick way to create lists, dict, sets or append instead using loops.
# my_list = [param for param in iterable]
# list comprehension

my_list = [char for char in 'hello']
my_list2 = [num for num in range(0, 100)]
# to multiply all the numbers of list with 2.
my_list3 = [num*2 for num in range(0, 100)]
# to square the number in the list and add only even numbers to the list.
my_list4 = [num*2 for num in range(0, 100) if num % 2 == 0]

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)


# Set Comprehensions.
# Just add the {} braces.

my_list = {char for char in 'hello'}
my_list2 = {num for num in range(0, 100)}
# to multiply all the numbers of set with 2.
my_list3 = {num*2 for num in range(0, 100)}
# to square the number in the list and add only even numbers to the set.
my_list4 = {num*2 for num in range(0, 100) if num % 2 == 0}

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

# dict comprehension.

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k: v**2 for k, v in simple_dict.items()}
print(my_dict)
my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(my_dict)

my_dict = {num: num*2 for num in [1, 2, 3]}
print(my_dict)

# Excercise:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
duplicates = list({char for char in some_list if some_list.count(char) > 1})
# enumerate(duplicates)
print(duplicates)
