# tuple

# It is kind of a list and immutable means we cannot change or replace the item using the index.

my_tuple = (1, 2, 3, 4, 5, 5)
print(my_tuple)

# we can check if an item is in the tuple

print(1 in my_tuple)

# we can assign the tuple to a new tuple variable and slice it like a list.

new_tuple = my_tuple[1:2]
print(new_tuple)

# to assign every item of the tuple to a single variable.
#x, y, z, *other = (1, 2, 3, 4, 5, 6)
# print(x)

x = my_tuple[0]
y = my_tuple[1]

print(x)
print(y)

# count method is used to count the number of times items are present in tuple
count_tuple = (1, 2, 3, 4, 5, 5, 2, 1)
print(count_tuple.count(5))

# index method is used to find the index value of an item in the tuple

index_tuple = (1, 2, 3, 4, 5, 5, 2, 1)
print(index_tuple.index(5))
