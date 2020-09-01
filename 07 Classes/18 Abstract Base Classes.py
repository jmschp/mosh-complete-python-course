# 18 Abstract Base Classes

from abc import ABC, abstractmethod


class InvalidOperationError(BaseException):
    pass


class Stream(ABC): # Direving the Stream() classe from the ABC() class we make it abstract
    def __init__(self):
        self.opened = False 

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False
    
    @abstractmethod # Here we solve the second issue with the abstract method. Making the read() method, mandatory for all the classe taht derive from the Stream() class
    def read(self): # We jsut need to ceate the method and pass
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from network")


# continuing with the example from the last class
# There are a couple os issues with this impementation
# The first issue is that we can creat a Stream object and call the "open()"" method

#stream = Stream()
#stream.open()

# Why is this an issue. Because this stream class is an abstract. What are we workind with a Network, File?
# We should not be able to directly creat an instance od the Stream() class.
# We should always sub class it. And then create an instance of the sub class, like FileStream() or NetworStream() in this example.


# The second issue looking at the implementation of the FileStream() and NetworStream() classes we have an read() method in both.
# If tomorow we need a new class like MemoryStream(), it also should have the read() written in the same way.

# to solve this problems we use an abstract base class
# importing ABC and abstractmethod, functions from the abc module.

class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory")
