# 1 - Lists

# Example of a list with strings
letters = ["a", "b", "c"]
print(letters)

# Exemple of a lis with interger
numbers = [1, 2, 3, 4]
print(numbers)

# Each item in this list is a list it self. This creates a mtraix that is a 2 dimesional list.
matrix = [[0, 1], [2, 3]]
print(matrix)

# Example how to creat list
zeros = [0] * 5
print(zeros)

# Concatanate lists
combined = zeros + letters
print(combined)

# Creat a list of a sequence of numbers, in this example from 5 to 20
list_range = list(range(5, 21))
print(list_range)

# Convert a string to a list
string_list = list("Python")
print(string_list)

# Check the number os item in a list
item_in_string_list = len(string_list)
print(item_in_string_list)
