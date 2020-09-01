# 02 Creating Classes

class Point: # to name classes we use Pascal naming convention for example "ClassName" withh each word in upper case letter and no underscore
    def draw(self): # The we difine a function and by convention every function in the class should have a least one paramether, and we call this paramether self.
        print("draw")


point = Point()
point.draw()
print(type((point))) 
# Prints <class '__main__.Point'> # __main__ is the name of our module

print(isinstance(point, Point)) # Somethime we have an object and want to see if that object is an instance of a given class
