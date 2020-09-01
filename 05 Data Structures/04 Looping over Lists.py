# 04 Looping over Lists

letters = ["a", "b", "c", "d"]

for letter in letters:
    print(letter)

# to get the index of each item use the built in function enumerate()
for letter in enumerate(letters):
    print(letter)
# we get a Tuple with two item the first the index , second the item it self

for index, letter in enumerate(letters):
    print(index, letter)
