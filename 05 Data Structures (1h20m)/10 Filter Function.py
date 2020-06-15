# 10 - Filter Function

items = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(items)
# another cenario to use a lambda function filter this list and only get the item with price above 10

filtered_price = list(filter(lambda index: index[1] >= 10, items))
print(filtered_price)