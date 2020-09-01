# 02 Handling Exceptions

# To handle exceptions we have to put the statment in a try block
# When Python sees a try block it will execute every statment in this block, if any of the statments throws an exception, the code in the excepton block will be executed.
#If no exception are thrown the code in the execption block will not be executed.

try: # try block
    age = int(input("Age: "))
except ValueError as ex: # In this cde we are handeling ValueError exception for non-numeric values. "as ex" we can add a variable that will include detais about the execption.
    print("You did no enter a valid age.")
    print(ex)
    print(type(ex))
else: # An optional else block can be added. The code we add here will be executed if no execptions occur
    print('No exceptions where thrown')

print("Executions continues") # Because we are handeling this exeption properly the line will be executed, and the program will note crash