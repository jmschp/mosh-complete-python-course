# 06 Raising Exceptions

# We can also raise exception in our on code

def calculate_xfactor(age): # This function raises an exceptio if we give it an invalid argumnte 0 or less
    if age <= 0:
        raise ValueError("Age can not be zero or less")
    return 10 /age # Age can not be zero or less

# calculate_xfactor(-1)

# If we run this program, it will crash an we will get the following error:

# File "c:\Users\jmigu\iCloudDrive\Os meus documentos\Educa��o\Code with Mosh\The Complete Python Course\HelloWorld\06 Exceptions (20m)\06 Raising Exceptions.py", line 10, in <module>
#     calculate_xfactor(-1)
#   File "c:\Users\jmigu\iCloudDrive\Os meus documentos\Educa��o\Code with Mosh\The Complete Python Course\HelloWorld\06 Exceptions (20m)\06 Raising Exceptions.py", line 7, in calculate_xfactor
#     raise ValueError("Age can not be zero or less")
# ValueError: Age can not be zero or less

# And this happens because we did not handle exception properly, We did not have a "try:" block.

try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# Raising execption it is not advised. It is costly