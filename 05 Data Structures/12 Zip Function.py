# 12 Zip Function

# #The zip function return a zip object that can combines iterables into tuples
# This function returns a list of tuples. The ith tuple contains the ith element from each of the argument sequences or iterables.
# If the argument sequences are of unequal lengths, then the returned list is truncated to the length of the shortest argument sequence.

list_1 = [1, 2, 3, 4]
list_2 = [10, 20, 30, 40, 50, 60]

combined_list = zip(list_1, list_2)
print(list(combined_list))

list_3 = list(zip("abcd", list_2, list_1))
print(list_3)