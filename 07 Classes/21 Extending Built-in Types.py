# 21 Extending Built-in Types

# In Python can also use inheritance with the built-in types.

class Text(str): # For example we can create a class called "Text()" and make it a sub class of "str". With this our text class will inherit all the features from the "str" class.
    def duplicate(self): # And we can add more feture to it. Like duplicate for example
        return self + self


text = Text("Python") # This text object will inherit all the features from "str" like ".lower()" to convert for lower case letters
print(text.duplicate()) # but we can also use the new fetures we created in the "Text()" class.


class TackableList(list): # In this example we are extending the built-in Python "list()"
    def append(self, object): # Adding features to the append method.
        print("Append called") # Like printing this message every time an object is appended. For logging for example
        super().append(object) # And we call the append method from the base class "List()" with the "super()" method.


object_list = TackableList()
object_list.append(1)
print(object_list)