# 20 Dictionary Comprehensions

# Dict comprehensions can be used to create dictionaries from arbitrary key and value expressions
# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
# {x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
# dict(sape=4139, guido=4127, jack=4098)
# {'sape': 4139, 'guido': 4127, 'jack': 4098}

valores = {x: x * 2 for x in range(5)}
print(valores)