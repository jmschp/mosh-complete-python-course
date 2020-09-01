# 08 For Loops

# They are used to reapet a task
# In this example we are trying to send a message to a use at least 3 time

for number in range(3):  # the range goes from 0, 1, 2
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):  # range goes from 1, 2, 3
    print("Attempt", number, number * ".")

for number in range(1, 10, 2):  # range goes from 1, 3, 5, 7, 9
    print("Attempt", number, number * ".")
