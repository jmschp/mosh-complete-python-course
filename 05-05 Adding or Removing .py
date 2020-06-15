# 5 - Adding or Removing Items

letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)

# Add an item to the end of the list
letters.append("h")
print(letters)

# Add item at a specific position using the method insert()
# first argumet position of the list, second argument iem to add
letters.insert(2, "-")
print(letters)

# Remove an item of a list use the method pop()
# with no argument it removes the last item
letters.pop()
print(letters)

# with a argument it removes the item with that index
letters.pop(2)
print(letters)

# Remove an item for a lsi using the method remove()
# specify the item
letters.remove("c")  # this will remove the first "c" in the list
print(letters)
# if there were multiple "c" we need to loop over the list

# Remove item using the del statement
# we this statement we can rmove one item or a range of items by theer index
del letters[0:2]
print(letters)

# to clear the list and delete all the items use the method clear
letters.clear()
print(letters)
