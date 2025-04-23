# Here is an example of input validation using the regex module

import re

email = input("Enter your email: ")
if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
    print("Valid email!")
else:
    print("Invalid email format.")

