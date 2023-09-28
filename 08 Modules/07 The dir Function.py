# 07 The dir Function

# With this fuction we can get the list of attributes and method defined in an object.

from ecommerce.shopping import eshopping

print(dir(eshopping))
# We will get this rersult:
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'shopping']
# As we can see above we have in the list the "shopping" method from the "eshopping.py" module.
# As well as other magic methods that are automataclly created.

print(eshopping.__name__) # That returns the name of our module
print(eshopping.__package__) # To get the name of the package that module belong to 
print(eshopping.__file__) # To get the path to the file on your system
