# 05 Class vs Instance Methods

# We have instance methods and Class methods
# Instances methods we call using an instance of the Point class. Using an object
# When we don't nedd an existing object we use a Class method.
# For example if we need to create a point with the initial values (0, 0 ,0)

class Point:
    point_color = "Red"

    @classmethod # This is what we call a decorater. We have to call to make this method a class method.
    def zero(cls): # By convention when we define a Class method its first argument should be cls. It is a reference to the class it self
        return cls(0, 0, 0)

    def __init__(self, x, y, z): # This is instance methods
        self.x = x
        self.y = y
        self.z = z

    def draw(self): # This is instance methods
        print(f"Point coordinates ({self.x}, {self.y}, {self.z})")


point_1 = Point(100, 200, 10)

point_2 = Point(500, 900, 100)

point_3 = Point.zero() # here we are using an Class method

point_1.draw() # here we are using an instance method. Use intance methods whenever we nedd an object reference
point_2.draw()
point_3.draw()