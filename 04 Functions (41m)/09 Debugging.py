# 9 - Debugging


def multiply(*numbers):  # Whit an * before the parameter we can add multiple arguments to creat a Tuple
    total = 1
    for number in numbers:
        total = total * number
        return total  # by indenting thsi stamente in the for loop we are simulating a bug


print("Start")
print(multiply(1, 2, 3))
