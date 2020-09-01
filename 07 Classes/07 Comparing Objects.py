# 07 Comparing Objects

# There are time we need to compare two objects created by a class

class Point:
    point_color = "Red"

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self): # This method is returning our point as a string
        return f"{self.x}, {self.y}, {self.z}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y and self.z > other.z
    
    def draw(self):
        print(f"Point coordinates ({self.x}, {self.y}, {self.z})")

point_1 = Point(100, 200, 10)

point_2 = Point(100, 200, 10)

point_3 = Point(200, 500, 100)

print(point_1 == point_2)
# If we don't have a magic method to compare objects implemented we will get false.
# The reason we get false is that by default this comparison operator compares the address of this two objects in memory.
# In this case this two variables are referencing two diferent objects in memory and tha's why they are not equal
# To solve this we nedd a magic method:
#  def __eq__(self, other):
#         return self.x == other.x and self.y == other.y and self.z == other.z


print(point_1 > point_3)
# If we want to compare if it is grater than, we also need to implemente a magic method "__gt__"
# If we don't implement this we will get an error: TypeError: '>' not supported between instances of 'Point' and 'Point'
# We don't have to explicity implement the magic method "__lt__" for < because Python will do it automatically