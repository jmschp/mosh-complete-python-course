# 16 Command-line Arguments

# If we want to create a Python program that expets command line argumments.

import sys # import the "sys" module to use the attribute ".argv"

# print(sys.argv)

if len(sys.argv) == 1:
    print("USAGE: python3 app.py <password>")
else:
    password = sys.argv[1]
    print("Password: ", password)