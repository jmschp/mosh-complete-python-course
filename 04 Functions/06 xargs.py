# 06 *args


# def multiply(x, y):  # this function acepts only 2 parameters x and y
#   return x * y


# multiply(2, 3)


def multiply(*numbers):  # Whit an * before the parameter we can add multiple arguments to creat a Tuple
    total = 1
    for number in numbers:
        total = total * number
    return total


print(multiply(1, 3, 6, 2, 8))
