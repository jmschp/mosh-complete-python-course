# 15 Multi-level Inheritance

# Multi-level can be a dangerous, and make the code to complex


class Animal:
    def __init__(self):
        self.age = 1
    
    def eat(self):
        print("eat")

class Bird(Animal):
    def fly(self):
        print("fly")

class Chicken(Bird): # The class chicken is inherace all the features of the "Bird" class, but a chicken can not fly
    pass

# it should be limited to one or two levels