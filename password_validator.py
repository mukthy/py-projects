# At least 8 char long
# contain any sort letters, numbers $%#@

import re

password = input('Enter the password \n')

if len(password) >= 8:
    password_pattern = re.compile(r"(^[a-zA-Z0-9.$%#@+]+$)")
    check_password = password_pattern.search(password)
    if check_password is None:
        print('Password must only contain letters, numbers and $%#@')
    else:
        print(f'Password is validated, it is {len(password)} characters long: {password}')

else:
    print('Password is less than 8 Characters')
