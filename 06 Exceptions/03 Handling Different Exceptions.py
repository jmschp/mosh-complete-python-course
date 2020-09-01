# 03 Handling Different Exceptions

try: # try block
    age = int(input("Age: "))
    xfactor = 10 / age # If age is 0 (a numeric value) this line will produce an error "ZeroDivisionError". We cann not divide a number by zero.
except (ValueError, ZeroDivisionError): # Better than add the another execption block below add the several exception between paranthesis.
    print("You did no enter a valid age.")
#except ZeroDivisionError: # We can add another exception, or add the "ZeroDivisionError" to the exception block above
#    print("Age can not be zero")
else: # An optional else block can be added. The code we add here will be executed if no execptions occur
    print('No exceptions where thrown')

print("Executions continues") # Because we are handeling this exeption properly the line will be executed, and the program will note crash