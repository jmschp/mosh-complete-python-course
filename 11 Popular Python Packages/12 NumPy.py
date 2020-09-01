# 12 NumPy

# We are going to take a look ate NumPy package. Which is heavily use in scientific computation.
# It is a package to work with Data Science and Machine Learning.
# To work with large array and multi dimension arrays, numpy is the best package

import numpy as np # We are importing "numpy" as an alias "np". So it is shorter to write in our code.

array_1 = np.array([1, 2, 3]) # To create a NumPy array
print(array_1)
print(type(array_1)) # This is a NumPy array.

array_2 = np.array([[1, 2, 3], [4, 5, 6]]) # To create a multidimension NumPy array. That it is called a matrix in math.
print(array_2)

print(array_2.shape) # With the shape attribute. We can get a tuple with the number of row and columns in our array.

array_zeros = np.zeros(shape=(4,4), dtype=int) # With the ".zeros()" method we can initialize a multidimension array of zeros.
print(array_zeros)

array_ones = np.ones(shape=(4,4), dtype=int) # With the ".ones()" method we can initialize a multidimension array of ones.
print(array_ones)

array_n = np.full(shape=(4,4), fill_value=5) # With the ".full()" method we can initialize a multidimension array with a specific number "fill_value".
print(array_n)

array_rand = np.random.random((4,4)) # We can initialize a random array, with values between 0.0 to 1.0 with the ".ramdom()" method from the "ramdom" module of NumPy.
print(array_rand)

print(array_rand[0, 2]) # To access a value in the array. In this case the value in row 0 and column 2.

print(array_rand > 0.3) # This will return an array of boolean values.

array_03 = array_rand[array_rand > 0.3] # This will return a new array with the numbers greater than 0.3
print(array_03)

total = np.sum(array_rand) # This will sum all the number in our array
print(total)

array_floor = np.floor(array_rand) # This will return a new array, with the same shape, with the floor of all the numbers
print(array_floor)

array_ceil = np.ceil(array_rand) # This will return a new array, with the same shape, with the ceil of all the numbers
print(array_ceil)

array_rounded = np.round(array_rand) # This will return a new array, with the same shape, with the rounded numbers.
print(array_rounded)

array_sum = array_1 + array_2 # We can sum two array together
print(array_sum)

array_add = array_2 + 2 # This will add a 2 to all the numbers in the array.
print(array_add)

dimensions_inch = np.array([10.45, 2.8, 3.9]) # we have an array of dimension in inches.
dimensions_cm = dimensions_inch * 2.54 # Here we convert the inches to cm. 
print(dimensions_cm)