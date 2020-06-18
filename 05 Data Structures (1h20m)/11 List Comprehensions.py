# 11 List Comprehensions

products = [
    ("Product1", 15),
    ("Product2", 50),
    ("Product3", 5)
]
print(products)


# prices = list(map(lambda item: item[1], products))
# print(prices)

prices = [item[1] for item in products] # With list comprehensions we can achive the same result with a clenaer code
print(prices)


# filtered_price = list(filter(lambda item: item[1] >= 10, products))
# print(filtered_price)

filtered_price = [item for item in products if item[1] >= 10]
print(filtered_price)