# 11 Working with Time Deltas

from datetime import datetime, timedelta
import time

# The datetime module supplies classes for manipulating dates and times.
# While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.
# https://docs.python.org/3/library/datetime.html

dt1 = datetime(1983, 6, 30, 18, 5, 54) # This is one way to create a "datetime" object
print(dt1)

dt2 = datetime.now() # This is a method from the "datetime" class that returns the current time.
print(dt2)

duration = dt2 - dt1
print(duration)
print("Days:", duration.days)
print("Seconds:", duration.seconds)
print("Total seconds:", duration.total_seconds())

# We can also add a "timedelta" object to a "datetime" object

dt3 = dt2 - timedelta(days=365)
print(dt3)