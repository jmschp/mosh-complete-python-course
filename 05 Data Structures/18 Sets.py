# 18 Sets

# Python also includes a data type for sets.
# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries.
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary.

numbers = [1, 1, 2, 5, 4, 5, 1, 2, 2, 1, 4, 5, 5]
uniques = set(numbers)
print(uniques)

# We can use the same methods as lists
uniques.add(6)
print(uniques)

uniques.remove(6)
print(uniques)

print(len(uniques))


# Sets shine with the matehmatical operator supported by them
first_set = {1, 2, 3, 4, 5}
second_set = {1, 2, 7, 8, 9}

print(first_set | second_set) # Unifies set.
print(first_set.union(second_set)) # Same as above.

print(first_set & second_set) # Gets the common objetcs in the set.
print(first_set.intersection(second_set)) # Sama As above.

print(first_set - second_set) # The diference between the first and the second set.
print(first_set.difference(second_set)) # Same as above.

print(second_set - first_set) # The diference between the second and the first set.
print(second_set.difference(first_set)) # Same as above.

print(first_set ^ second_set) # Symetric difference retun the items, ruturns the items that are either in the first and second, but not both.
print(first_set.symmetric_difference(second_set)) # Same as above.

