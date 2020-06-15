# 21 Generator Expressions

# A generator expression is a compact generator notation in parentheses:
# generator_expression ::=  "(" expression comp_for ")"
# A generator expression yields a new generator object.
# Its syntax is the same as for comprehensions, except that it is enclosed in parentheses instead of brackets or curly braces.

# Unlike list they don't store all the values in the memory, they generate a value in each interation.

from sys import getsizeof # import getsizeof function

values = (x * 2 for x in range(100))
print(values) # prints the genarator object


# for x in values:
#     print(x)

print(getsizeof(values)) # show the bites of memory