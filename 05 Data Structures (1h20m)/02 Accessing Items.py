# 2 - Accessing Items

#  a   b   c   d - example list
#  0   1   2   3 - position of each item in the list
# -4  -3  -2  -1 - or position of the item ins reverse
letters = ["a", "b", "c", "d"]
print(letters)

first_item = letters[0]  # to access the item number 0 in the list
print(first_item)

letters[0] = "A"  # to change the first item in the list

print(letters)

numbers = list(range(20))
print(numbers)

# Like string this is o slice a list [first item : last item: step] all argumente are optinal
numbers_slice = numbers[2:15:2]
print(numbers_slice)

# with this we are able to reverse the order of the list
numbers_revers = numbers[::-1]
print(numbers_revers)
