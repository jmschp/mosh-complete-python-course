# # # 12 - Exercise

# write a function that recieves an integer as an inputa and returns the following:
# For each multiple of 3, print "Fizz" instead of the number.
# For each multiple of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 != 0):
        print("Fizz")
    elif (input % 3 != 0) and (input % 5 == 0):
        print("Buzz")
    elif (input % 3 == 0) and (input % 5 == 0):
        print("FizzBuzz")
    else:
        print(input)


fizz_buzz(7)


# Mosh anwser


def fizz_buzz_mosh(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif (input % 3 != 0):
        return "Fizz"
    elif (input % 5 == 0):
        return "Buzz"
    return input


print(fizz_buzz_mosh(15))
