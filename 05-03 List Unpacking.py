# 3 - List Unpacking

numbers = [1, 2, 3]
print(numbers)

# Assigning an item of a list to a variable
# first = numbers[0]
# second = numbers[1]
# third = numbers[3]

# The best way to this is by list unpacking
first, second, third = numbers
print(first)
print(second)
print(third)
# this is the same as the code in lines 6, 7, 8. The number of item in the left side of = most be the same as th number of items in the lis.

# If we have alist with a lot of item and we just want to unpack the first two item and pack the rest os item in another list
numbers_0_19 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
                10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(numbers_0_19)
first, second, *others = numbers_0_19
print(first)
print(second)
print(others)

# For example if we want the unpack the first and the the last item
first, *others, last = numbers_0_19
print(first)
print(others)
print(last)
