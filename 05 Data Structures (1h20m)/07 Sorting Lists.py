# 7 - Sorting Lists

numbers = [5, 51, 2, 15, 6]
print(numbers)

# sort numbers in use the sort() method
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

# The sort function can be used an it will creat a new list
print(sorted(numbers))
print(sorted(numbers, reverse=True))


# List of complex objects, like a list of tuples, example a list of orders with product name and price
# in situations like this we need to define a function  to sort the list, the above methods don't work
items = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(items)

# In this example we are going to sort the items base in price


def sort_items_price(index):
    return index[1]
# if each item in the list is a tuple we are returning the second item in the tuple


items.sort(key=sort_items_price)
print(items)
