# 14 Method Overriding


class Animal:
    def __init__(self):
        self.age = 1
    
    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        self.weight = 1
        super().__init__() # If we don't add the supper function the constroctor in the Animal class will not be executed because it will be replace by the contructor 
        # With the super() we can acess any method on the animal class

    def walk(self):
        print("walk")

