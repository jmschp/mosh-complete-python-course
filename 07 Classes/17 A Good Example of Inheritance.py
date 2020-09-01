# 17 A Good Example of Inheritance

# A good example of inheritance, would be modeling how to read a stream of data
# A stream of data can come from multiple sources, a file, network, memory etc.
# They all have features in commom like opening or closing the stream. But how we read data from then chages from one to another.

class InvalidOperationError(BaseException): # Creatin a costum error. By convention all costum exceptions should en with "Error". And every time we create a costum exception in a class, we should derive the exception from the Base exeption.
    pass


class Stream: # Here we are defining a class with the comom fetures between the streams, like open and close.
    def __init__(self):
        self.opened = False # Create a constructor ans set an opened flag initily to false.

    def open(self): # if we try to open a stream taht is already opened, that an invalid operation. So we can rais ean exception
        if self.opened:
            raise InvalidOperationError("Stream is already open") # Because in Python we don't have a built in exception for this we can create a costum exception 
        self.opened = True

    def close(self): 
        if not self.opened: # Here we check if the stream is alredy closed. If it is closed and we try to close it we will raise an invalid operation error.
            raise InvalidOperationError("Stream is already closed")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading data from file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


# This is a good example of inheritance
# We dont't ahev multy level inheritance
# We only have two levels of inherante
# And we don't have multiple inheritance