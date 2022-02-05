username = input('\nEnter your username: ')
password = input('\nEnter your password: ')

password_length = len(password)

encoded = '*' * password_length

print(f"\n{username}, your passowrd {encoded} is {password_length} letters long\n")
