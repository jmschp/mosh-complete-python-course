# 06 Magic Methods

# https://rszalski.github.io/magicmethods/

# Magiv Methods are called automaticly by Python interpreter, depending on how we use our object and class

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

    def draw(self):
        print(f"Point coordinates ({self.x}, {self.y}, {self.z})")

point_1 = Point(100, 200, 10)
print(point_1)