# 15 Tuples

# Tuples are basiclly read only lists, can not be change

points = (1, 2, 3) # with paretesis it is a Tuple
print(type(points))

points_1 = (1, 2, 3, 4, 5) + (6, 7, 8, 9) # Concateante a tuple
print(points_1)

points_2 = (1, 2, 3, 4, 5) * 3 # multiply a tuple
print(points_2)

text_tuple = tuple("Hello World") # Because a strinf is an itarable it can be converted to a tuple with the built in function tuple()
print(text_tuple)

# Tuple can be trasnformed into a list with the built in list function
print(list(points_1))

# Like list ww can acsses a iem by theindex
print(points[1])

# Unpack tuple
x, y, z = points
print(f"x: {x}\ny: {y}\nz: {z}")

# Check if an item is in the Tuple
if 2 in points:
    print("Exists")
else:
    print("Not there")