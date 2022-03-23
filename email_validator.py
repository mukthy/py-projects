import re

email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

email = input('Enter your email address\n')

check_email = email_pattern.search(email)

if check_email is None:
    print("Invalid Email")

else:
    print(check_email.group() + " is a Valid Email")
