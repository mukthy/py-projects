# Lambda function is anonymous and only used once.
# lambda param: action(param)

from functools import reduce


my_list = [1, 2, 3]

print(list(map(lambda item: item * 2, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))
print(reduce(lambda acc, item: acc + item, my_list, 0))

print(list(map(lambda item: item * item, my_list)))
print(my_list)

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
# a.sort()
a.sort(key=lambda i: i[1])
print(a)
