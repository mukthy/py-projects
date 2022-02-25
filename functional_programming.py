# Functional Programming:

# 1: given the same input it will always return the same output. Forex : below function will always return 2,4,6 for the input of 1,2,3.
# 2: Does the function produce any sideeffect or does this function touch anythin on the outside world.
# 3: Does the function access out of scope or variables or values out side of the function.

from functools import reduce


def multiplyby_2(li):
    new_list = []
    for item in li:
        new_item = item * 2
        new_list.append(new_item)
    return new_list


print('1', multiplyby_2([1, 2, 3]))

# map() function
# map(action, iterables)
new_lst = [1, 2, 3]
your_lst = [5, 6, 7]
their_lst = [8, 9, 10]


def multi_by2(item):
    return item * 2


print('2', list(map(multi_by2, new_lst)))
print(new_lst)

# filter()
# to filter our some output.


def only_odd(item):
    return item % 2 != 0


print('Only ODD:', list(filter(only_odd, new_lst)))
print(new_lst)


# Zip()
# zip(iterables, iterables) Zip the items together.
# it zips the first element of the new_lst and first element of your_lst into a tuple.
print(list(zip(new_lst, your_lst, their_lst)))


# reduce()
# reduce(function, iterable, initial)

def accumulator(accu, item):
    return accu + item


print(reduce(accumulator, new_lst, 0))
