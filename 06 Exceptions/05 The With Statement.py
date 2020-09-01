# 05 The With Statement

# We have a shoter and cleaner way to achive the same thing as the finally block.
# But it only works with certain objects

try:
    with open("05 The With Statement.py") as file: # In here we are opening a file with the "with" function and storing it in the variable file.
        print('File open') # When ever we open a file with the "with" statment Python will automatically close that file whether we have a finally block or not
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You did no enter a valid age.")
else: 
    print('No exceptions where thrown')

# If an object as this two methods we say that object supports context management protocol.
# And we can use it with the "with" statment. And Python will automatically call the exit method and realese external resourses
# file.__enter__
# file.__exit__

# Some times we can be working the several files
# with open("05 The With Statement.py") as file, open("04 Cleaning Up.py") as file2: