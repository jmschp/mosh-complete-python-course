# 16 Multiple Inheritance

# In Pyhton a class can have multiple Base classes
# But like Multi-level Inheritance it should be used with caution.
# If not used properly it will crat bug in the progam

class Employee:
    def greet(self):
        print("Greet Employee")


class Person:
    def greet(self):
        print("Greet Person")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()
# We will get Greet Employee, because the Employee class is called first.
#If the Employee class didn't have the greet method then the greet method in the person class would be called.


# It is better to use multiple Inheritance, with classes small classes that have nothing in common.


# This is a better example of multiple inheritance.
class Flyer: # here we are setting a classe and creating a feature for flying
    def fly(self):
        pass


class Swimmer: # here we are setting a classe and creating a feature for swiming
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer): # So the FlyingFish class can inherit the features fo the Flyer and Swimer classes.
    pass