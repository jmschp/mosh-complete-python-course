# 03 Constructors

# When creatiing a point object and we want to provide x, y z coordinates.
# To achive this we need a constructor, which is special method that is called when we create a new point object.

class Point:
    def __init__(self, x, y, z): # To create a constructor we call the magic method "__init__". "Self" is a reference to the current object, so we use self to set the atributes
        self.x = x # x, y, z are attributes of the point object
        self.y = y
        self.z = z

    def draw(self):
        print(f"Point coordinates ({self.x}, {self.y}, {self.z})")


point = Point(100, 200, 10)
print(point.x)
point.draw() # When calling the ".draw" method we did not have to suply a paramater because Python does that by default.