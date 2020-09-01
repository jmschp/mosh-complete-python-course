# 22 Data Classes

from collections import namedtuple

# We use classes to bundle data and functionalatie into one unit.
# In some cases we may come across with classes that don't have any behavior like functions. And only have data

# Like in this example
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# With this we can create point objects

p1 = Point(1, 2, 3)
p2 = Point(1, 2, 3)
# print(p1 == p2) # But when using this, it will return False, because the two objects are stored in diferent locations of the memory
# print(id(p1)) # To see where they are stored in memory use the "id()" funtions that returns memory address.
# print(id(p2)) # To solve this issue we must implement a magic method like the ones seen on leson 08 Performing Arithmetic Operations.

# When dealing with classes that have no behavior, and just have data, whe can use namedtuple instead.
# Importing form the "collection" module the "namedtuple()" function

Point_t = namedtuple("Point", ['x', "y", "z"]) # The first argument we specify the label for the the new type we want to create. The second argument we pass an array of field names or atribute names. 
p4 = Point_t(x=1, y=2, z=3)
p5 = Point_t(x=1, y=2, z=3)
print(p4 == p5)
print(p4)
print(p4.x)
# If working with classes, that only contain data it is usual better to use "nametuple()"
# Our code is more clear and less ambigues
# And also that we do not ness to create a magic method to compare two objects.