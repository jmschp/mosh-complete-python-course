# 12 Zip Function

#The zip function return a zip object that can combines iterables into tuples

list_1 = [1, 2, 3, 4]
list_2 = [10, 20, 30, 40]

combined_list = zip(list_1, list_2)
print(list(combined_list))

list_3 = list(zip("abcd", list_2, list_1))
print(list_3)