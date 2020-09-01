# 10 Working with DateTimes

from datetime import datetime
import time

# The datetime module supplies classes for manipulating dates and times.
# While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.
# https://docs.python.org/3/library/datetime.html

dt1 = datetime(1983, 6, 30, 18, 5, 54) # This is one way to create a "datetime" object
print(dt1)

dt2 = datetime.now() # This is a method from the "datetime" class that returns the current time.
print(dt2)

dt3 = datetime.strptime("29/06/2020", "%d/%m/%Y") # This is a method to convert a string into a "datetime" object. For example to convert input from a user.
print(dt3)

dt4 = datetime.fromtimestamp(time.time()) # With the ".fromtimestamp()" method we can convert a time stamp to "datetime" object.
print(dt4)

print(f"{dt2.year}/{dt2.month}") # An example of the method avaiable in a "datetime" object.

dt5 = dt2.strftime("%Y/%m/%d") # this method is the opposite of the ".strptime()" method. To convert a "daytime" object into a string.
print(dt5)

print(dt2 > dt1) # We can also perfotm compare operation in "datetime" objects.