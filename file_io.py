# my_file = open('test.txt')
# print(my_file.read())
# this helps to reset the cursor back to 0
# my_file.seek(0)
# print(my_file.read())

# print(my_file.readline())  # this prints the first line of the file

# print(my_file.readlines())  # this prints all the lines of the file
# my_file.close()

# with open('test.txt', 'a') as my_file:
#     text = my_file.write('It is appended')
#     print(text)
#     # print(my_file.readlines())

try:
    with open('sad.txt'):
        print(my_file.read())
except FileNotFoundError as err:
    print('file does not exist')
    raise err
