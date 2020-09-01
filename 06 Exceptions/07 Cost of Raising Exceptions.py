# 07 Cost of Raising Exceptions

# Exception come with a cost

from timeit import timeit # from the "timeit" module import the function called "timeit" that can calculated how long it takes to execute a python code.

code_1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be zero or less")
    return 10 /age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

code_2 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age can not be zero or less")
    return 10 /age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code_3 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 /age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""

print("Code 1 execution time: ", timeit(code_1, number=10000)) # 1.9712759
print("Code 2 execution time: ", timeit(code_2, number=10000)) # 0.005862399999999823
print("Code 3 execution time: ", timeit(code_3, number=10000)) # 0.0021092000000000333

# As we can see by the executions times the "code_3" is much faster because it does not raise an execption.