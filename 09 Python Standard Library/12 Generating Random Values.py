# 12 Generating Random Values

import random
import string

# With this module we can generate random values

rand1 = random.random() # The generates a float between 0 and 1.
print(rand1)

rand2 = random.randint(1, 10) # The generates an integer between two numbers. In this case 1 and 10.
print(rand2)

rand3 = random.random() # The generates a float between 0 and 1.
print(rand3)

rand4 = random.choice([1, 2, 3, 4, 5, 6]) # This method pick a number in a list.
print(rand4)

rand5 = random.choice(list(range(101)))
print(rand5)

rand6 = random.choices([1, 2, 3, 4, 5, 6], k=4) # With this method we can select how many item it will be selected from the list
print(rand6)

# In case we want to generate a random password, with letter abd number.
# Import the string module

print(string.ascii_letters) # this method will return a string with the alpahbet both in loer case and upper case. "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(string.digits) # this method will return a string with the number from 0 to 9. "0123456789"

password = "".join(random.choices(string.ascii_letters + string.digits, k=6)) # We use the ".join()" method with an empty string to join all the item of the selected list
print(password)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(numbers) # With this method shuffle an array.
print(numbers)