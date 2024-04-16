import re

email = input("Enter your email for validation: ")
email_condition = "^[a-z]+[\._]?[a-z 09]+[@]\w+[.]\w{2,3}$"

if re.search(email_condition, email):
    print("Valid Email")
else:
    print("Invalid Email")