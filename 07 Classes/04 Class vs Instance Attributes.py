# 04 Class vs Instance Attributes


class Point:
    point_color = "Red" # This is a class atribute, defined at the class level. And they are the same across all instances of the class.

    def __init__(self, x, y, z): # "x, y, z" This are instance atributes. In other other this are attributes that belong to point instance or point objects. # every point object can have different values for this atributes.
        self.x = x
        self.y = y
        self.z = z

    def draw(self):
        print(f"Point coordinates ({self.x}, {self.y}, {self.z})")


point_1 = Point(100, 200, 10)

# We can also define an atribute after we create a point object. Because objects are dynamic in Python we don't have to define all the atributes in the contructor.
# But ony this point will have this atribute
point_1.tipo = "Controle"

print(point_1.x)
print(point_1.tipo)
point_1.draw()

point_2 = Point(500, 900, 100)
print(point_2.x)
point_2.draw()

print(point_1.point_color) # We can use this object reference to get acess to the point color atribute (which is a defualt class atribute)
print(Point.point_color) # In here we are using the Point Class to get acess to the point color atribute

Point.point_color = "Blue" # In here we change the Class atribute Point Color to blue 

print(point_2.point_color)

point_1.point_color = "Yellow" # In here we change the point color of thsi ofject but the Class Point color does not change. 