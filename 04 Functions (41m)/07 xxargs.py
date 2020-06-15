# 7 - **args


def save_user(**user):  # Function to save information abpout a user
    print(user)


# Here we are passing 3 Keyword Arguments to this function.
save_user(id="V857093-N", name="Jose", age=36)
# {'id': 'V857093-N', 'name': 'Jose', 'age': 36} This will return a dictionary, witch is a complex object.
