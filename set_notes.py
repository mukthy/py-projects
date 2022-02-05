# SET

# set is kind of a dictionary but without keys, it only has values. It is an
# unordered collection of unique objects. That means it cannot have a duplicate item.

from re import sub


my_set = {1, 2, 3, 4, 5, 6, 6}
my_set.add(7)  # 7 gets added to the set.
# it will not add 3 to the set because it is already present and set does not allow duplication
my_set.add(3)

print(my_set)

# to convert a list to a set which can also have unique
my_list = [1, 2, 3, 4, 5, 5]

new_set = set(my_list)
print(new_set)

# it does not support index so we need to grab it with the value
# So we need to loop through the set of items or check if the items are present using 'in' keyword.

print(1 in my_set)

# we can convert a set to a list

print(list(my_set))

# we can copy a set to a new set variable

new = my_set.copy()

# my_set.clear()  # to clear a set.
print(new)
print(my_set)


i_set = {1, 2, 3, 4, 5}
sub_set = {4, 5}
u_set = {4, 5, 6, 7, 8, 9, 10}

# to find a difference between two sets, we have to use difference() method. It will return only the difference by ignoring the duplicates.
# this difference method does not update or modify the set.
print(u_set.difference(i_set))
print(i_set.difference(u_set))
print(i_set)
# to discard an item from the set, it also modifies the set.

# i_set.discard(5)
# print(i_set)

# this difference_update method will modify the set and remove the difference.
# i_set.difference_update(u_set)
print(i_set)

# to find an intersection in two sets.

print(i_set.intersection(u_set))
print(i_set & u_set)

# to find if boths sets have nothing in common

print(i_set.isdisjoint(u_set))

# to get union of the sets.

print(i_set.union(u_set))

print(i_set | u_set)

# to find if the sub_set is a subset of u_set

print(sub_set.issubset(u_set))

# to find if the u_set is a superset of sub_set

print(u_set.issuperset(sub_set))
