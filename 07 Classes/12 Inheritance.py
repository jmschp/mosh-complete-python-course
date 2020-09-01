# 12 Inheritance

# To don't reapet the same method in several classes we can use inheritance.
# It is a mechanism that allows us to define the common functions in onde classes and the inherit the in other classes

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal): # Here the Mammal class is inheriting the function and atributes from the Animal class
    # def eat(self): # And so we do not need to repeat the same function
    #     print("eat")
    
    def walk(self):
        print("walk")


class Fish(Animal): # Here the Fish class is inheriting the function and atributes from the Animal class
    # def eat(self): # And so we do not need to repeat the same function
    #     print("eat")
    
    def swim(self):
        print("swim")

m = Mammal()
m.eat()  # the Mammal class is using the eat funtion from the Animal class

f = Fish()
print(f.age) # The Fish class is using the age atribute from the Animal class 

# The Animal class is called the Parent or Base class
# The Fish and Mammal classes are the Child or Sub class