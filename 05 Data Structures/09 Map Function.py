# 09 Map Function

items = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(items)

# Transform this list in a simple list of numbers, with just the price
# prices = []
# for index in items:
#     prices.append(index[1])
# print(prices)

# there is a better more cleaner way to achive the same result with the map() function
prices = map(lambda index: index[1], items)
print(prices)
for index in prices:  # this way we loop the map function
    print(index)

# to create a list with just the prices use the list function
prices = list(map(lambda index: index[1], items))
print(prices)
