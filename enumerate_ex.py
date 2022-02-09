# enumerate will give the output of the index value and the value that is store at that index value.
for i, char in enumerate("helllllo"):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(i)
    else:
        pass
 