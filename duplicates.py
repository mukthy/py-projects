from hashlib import new


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# print(some_list)
new_list = []
for letter in some_list:
    n = some_list.count(letter)
    if n > 1:
        if letter not in new_list:
            new_list.append(letter)
print(new_list)


#dict_list = set(some_list)
#new_list = list(dict_list)
# new_list.sort()
# print(new_list)
