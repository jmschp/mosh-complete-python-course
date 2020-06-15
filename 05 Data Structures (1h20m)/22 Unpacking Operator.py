# 22 Unpacking Operator

numbers = [1, 2, 3]
print(numbers)
print(*numbers) # with * operator we are unpacking the list and passign them as single elements to the print function


values = list((range(10)))
print(values)
values  = [*range(10)] # With this operator we can unpack any iterables
print(values)

my_text = [*"Hello Miguel"]
print(my_text)

# We can combine multiple list
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
combined_lists = [*list_1, *list_2]
print(combined_lists)


# we can also unpack dictonaries but we have to use **

dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 4, "c": 6}
combined_dict = {**dict_1, **dict_2} # If we have multiple values with the same key the last valeu will be used
print(combined_dict)