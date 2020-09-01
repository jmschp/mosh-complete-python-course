# 04 Cleaning Up

# There are time we need to work with external resourses, like files, data bases, network connection or something else.
# When ever we use this resourses after we are donme we need to realese then. For exemple when we open a file we schould always close ti afer we are done.

try:
    file = open("04 Cleaning Up.py") # In here we are opening a file and storing it in the variable file.
    age = int(input("Age: "))
    xfactor = 10 / age
#    file.close() # Here wea are closing the file. But if an execption accur in line 8 or 9 the line will not be executed
except (ValueError, ZeroDivisionError):
    print("You did no enter a valid age.")
else: 
    print('No exceptions where thrown')
finally: # This finally block is alwys executed where we have an execption or not.
    file.close() # This is a better place to relase resourses


print("Executions continues")