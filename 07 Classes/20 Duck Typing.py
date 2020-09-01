# 20 Duck Typing

# With the example from the last class.
# Because Python is a dynamic typed language, we do not necessarily the UIContorl class


# from abc import ABC, abstractmethod

# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

class TextBox():
    def draw(self):
        print("TextBox")


class DropDownList():
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
       control.draw()

# With this change we can still achive Polymorpgic behavior
# In the "draw()" funtion we do not specify the type of the "contols" parameter, it is just a label.
# We just need to pass to it an iterable object. Like a list or tuple, for example
# And each item of that object must have the "draw()" method.
# As long as this objects have a "draw()" meyhod Python will be happy.
# This is what it is called Duck Typing. So if walks like a duck and quaks like a duck it is a duck.
# But having that "UIContol()" class its a good practice because it enforces a commom interface in its derivatives.