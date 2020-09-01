# 01 Classes

# https://docs.python.org/3/tutorial/classes.html
# Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made.
# Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.
# Compared with other programming languages, Python’s class mechanism adds classes with a minimum of new syntax and semantics.
# It is a mixture of the class mechanisms found in C++ and Modula-3.
# Python classes provide all the standard features of Object Oriented Programming:
#     the class inheritance mechanism allows multiple base classes,
#     a derived class can override any methods of its base class or classes,
#     and a method can call the method of a base class with the same name.
# Objects can contain arbitrary amounts and kinds of data.
# As is true for modules, classes partake of the dynamic nature of Python: they are created at runtime, and can be modified further after creation.
# In C++ terminology, normally class members (including the data members) are public (except see below Private Variables), and all member functions are virtual.
# As in Modula-3, there are no shorthands for referencing the object’s members from its methods: the method function is declared with an explicit first argument representing the object, which is provided implicitly by the call.
# As in Smalltalk, classes themselves are objects. This provides semantics for importing and renaming. Unlike C++ and Modula-3, built-in types can be used as base classes for extension by the user.
# Also, like in C++, most built-in operators with special syntax (arithmetic operators, subscripting etc.) can be redefined for class instances.

# Class is a blueprint for creatinf new objects
# An object is an instance of a class

# As an example
# Class: Human - We could have a classe called humans and this class would difine all the atributes of humans
# Objects: John, Miguel, Mosh 