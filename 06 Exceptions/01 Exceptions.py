# 01 Exceptions

# Errors detected during execution are called exceptions.

# Errors and Exceptions
# https://docs.python.org/3/tutorial/errors.html

# Built-in Exceptions
# https://docs.python.org/3/library/exceptions.html

numbers = [1, 2]
print(number[3])

# With this program we get an error because de list does not have index 3
# File "c:\Users\jmigu\iCloudDrive\Os meus documentos\Educa��o\Code with Mosh\The Complete Python Course\HelloWorld\06 Exceptions (20m)\01 Exceptions.py", line 10, in <module>
#     print(numnbers[3])
# IndexError: list index out of range

age = int(input("Age: "))

# With this code we will get an error if we enter a non-numeric value
# File "c:/Users/jmigu/iCloudDrive/Os meus documentos/Educação/Code with Mosh/The Complete Python Course/HelloWorld/06 Exceptions (20m)/01 Exceptions.py", line 17, in <module>
#     age = int(input("Age: "))
# ValueError: invalid literal for int() with base 10: 'a'

