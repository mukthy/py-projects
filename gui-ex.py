picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# print(picture)
zer = ' '
one = '*'
for items in picture:
    for index, item in enumerate(items):
        if item == 0:
            items[index] = zer
        elif item == 1:
            items[index] = one
    print(' '.join(items))
