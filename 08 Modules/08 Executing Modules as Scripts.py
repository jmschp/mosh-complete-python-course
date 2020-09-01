# 08 Executing Modules as Scripts

# In our "esales.py" module we have two functions.
# But we can also write any statments, and they will be executed the first time that module is loaded.
# Now we add a statment there "print("Sales initialized")"
# When we inmport that module Python will load that module only once and then cache it in memory. So the statments we rigth ther will be executed once
# Using the same technic we can write the code to initialize our packages in the "__init__.py" file

# In this example if we add the magic method "__name__" to the "print("Sales initialized", __name__)"
# Here we will see the name of the module, but if we run the file in "esales.py" we will get "Sales initialized __main__"
# The name of the module that starts our program is always "__main__"

from ecommerce import esales