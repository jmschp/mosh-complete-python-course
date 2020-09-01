# 19 Polymorphism

from abc import ABC, abstractmethod

class UIControl(ABC): # Here we are defining an abstract class with an abstract method.
    @abstractmethod
    def draw(self): # This abstract method with the decorater "@abstractmethod" difines the common feature or method that must be implemented in the the class that derive from  "UIControl()".
        pass

class TextBox(UIControl): # Here we define a class deriving from "UIControl()".
    def draw(self):
        print("TextBox")


class DropDownList(UIControl): # Here we define another class derivign from "UIContorl()".
    def draw(self):
        print("DropDownList")


# def draw(control): # Here we also have a funtion called draw, tjat takes a controle object and call the draw method in that object.
#     control.draw()

ddl = DropDownList() #here we create a DropDownList object by istanciate the "DropDownList()" in the variable "ddl".
print(isinstance(ddl, UIControl)) # Because the "DropDownList()" class derives from the class "UIControl()" the "ddl" object is an istance of the "UIControl()" class.

tb = TextBox()
print(isinstance(tb, UIControl))

# draw(ddl) # Here we apply the function draw in the variable "ddl" that will call the drw mehtod from the "dropDownList()" class.
# draw(tb)

def draw(controls): # Here we would implment a function that takes an iteable like a list or a tuple and iterates over it with a for loop.
    for control in controls: # In each iterations it will call the "draw()" method from "DropDownList()" or "TextBox()", depending on each obect it iterates.
       control.draw()

draw([ddl, tb]) # Passing the list to the function "draw()",

# Using this aproach we can render the user interface of an application
# Imagem that we have a form with Bottons, text boxes, drop down list, and so on.
# We could have a list with all this objects and pass that list to a function like the one above, ant it would render the intire from.
# The function does not know what kind of contorl is working with. This is detemined at runtime.
# It simples iterates over the list of controls and call the the "draw()" of each contol.
# This is called Polymorphism - Poly means many and morph forms - so many forms.
# To achive Polymorphic behavior, we start by defing a base class, in this example "UIControl()" and there we define the commom method we need in its derivates or children.
# And the we achive polymorphic behavior with the "draw()" function, here in line 32.
# This is how polymorphims works in pretty much all languages that support classes.