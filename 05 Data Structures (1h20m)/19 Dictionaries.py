# # 19 Dictionaries
# Another useful data type built into Python is the dictionary (see Mapping Types — dict).
# Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”.
# Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.
# Tuples can be used as keys if they contain only strings, numbers, or tuples;# if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
# You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments, or methods like append() and extend().
# It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary).
# A pair of braces creates an empty dictionary: {}.
# Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.
# The main operations on a dictionary are storing a value with some key and extracting the value given the key.
# It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten.
# It is an error to extract a value using a non-existent key.
# Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order (if you want it sorted, just use sorted(d) instead).
# To check whether a single key is in the dictionary, use the in keyword.

# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

point = {"x": 1, "y": 2}
point = dict(x=1, y=2) # Defining a dictonari with the dict() function.
print(point)
print(point["x"]) # To acsse an item in a dictonary we use its key

point["x"] = 10 # Changing the value in the dictonary of the key x
print(point)

point["z"] = 3 # Adding a kez "z" with value 3 to the dictonary
print(point)

# to look if a key is in the dictonary
if "a" in point:
    print("yes")

# or the get method
print(point.get("a")) # If the key does not exist we wil get None

# del point["x"] # to delete the key x
print(point)

for key in point: # Loop over dictoanaries, in here we will print the dictonary keys
    print(key)

for key in point: # Loop over dictoanaries, in here we will print the dictonary keys and the value
    print(key, point[key])

for index in point.items(): # with this lop we will get a tuple with the key and the value
    print(index)

for key, valeu in point.items():
    print(key, valeu)

print(point.items())