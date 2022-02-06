# The == operator checks if both the values that are given for comparison is the same

print(True == True)
print('1' == '1')
print([] == 1)
print(10 == 10.0)
print([1, 2, 3] == [1, 2, 3])

# The is operator actually checks if the location in memory where these values are stored are same.
print(True is True)
print('1' is '1')
# both the lists are stored in a different memory spaces or locations to it will always return False.
print([] is [])
print(10 is 10.0)
print([1, 2, 3] is [1, 2, 3])
