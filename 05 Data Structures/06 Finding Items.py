# 06 Finding Items

letters = ["a", "b", "c", "d", "e", "f", "g"]

# to find the index of a give item in a list use the index method
print(letters.index("d"))
# if the item passed to the method index() does not exist in the list we will get an error.
# it is best to first check if that item exits on the list

# Example 1
if "d" in letters:
    print(letters.index("d"))

# Exemple 2
print(letters.count("m"))

