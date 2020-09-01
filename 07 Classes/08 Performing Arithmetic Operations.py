# 08 Performing Arithmetic Operations

# We also have magic methods to perform artithemetic operations

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
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z) # we are returning a new point object adding the atributes

    
    def draw(self):
        print(f"Point coordinates ({self.x}, {self.y}, {self.z})")

point_1 = Point(100, 200, 10)

point_2 = Point(100, 200, 10)

print(point_1 + point_2)
# If don't implement the magic method "__add__" fo + we will get an error TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
# And if we don't have the "__str__" magic method implemented we eill see the ne point object memory address

point_3 = point_1 + point_2
print(point_3.x)