# 08 Lambda Functions

# List of complex objects, like a list of tuples, example a list of orders with product name and price
# in situations like this we need to define a function  to sort the list, the above methos don't work
items = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(items)

# In this exeample we are going to sort the items base in price

# def sort_items_price(index):
#    return index[1]
# if each item in the list is a tuple we are returning the second item in the tuple

# items.sort(key=sort_items_price)
# print(items)

# with a lambda or anonymous functions it's short and cleaner way to define a function that we are going to use only once as an argument of another function.
items.sort(key=lambda index: index[1])  # lambda parameter_list: expression
print(items)
