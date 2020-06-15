# 3 - Types of Functions

# 1 - Function that perform a task


def greet(name):
    print(f"Hi {name}")


greet("Miguel")


# 2 - Functions that return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Pimenta")
print(message)
