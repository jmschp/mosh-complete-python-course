# 11 Properties

# When we want to have controle over an atribute in the class.
# In this example we want to restric the price to positive values

class Product_1:
    def __init__(self, price):
        self.set_price(price) # We change the constructor from "self.price = price" to the set price function

    def get_price(self): # Here we are returning the price
        return self.__price
    
    def set_price(self, value): # In here if we try to set the price to a negative value we will raise an exception
        if value < 0:
            raise ValueError("Price can not be negative")
        else:
            self.__price = value

# product = Product(-50) # If we try to set the price to -50 we will throw an exception

# This is a simple solutiuon but it is not a Pythonic solution



# To improve this call in a Pythonic way we should use propreties "property()"


class Product_2:
    def __init__(self, price):
        self.set_price(price) # We change the constructor from "self.price = price" to the set price function

    def get_price(self): # Here we are returning the price
        return self.__price
    
    def set_price(self, value): # In here if we try to set the price to a negative value we will raise an exception
        if value < 0:
            raise ValueError("Price can not be negative")
        else:
            self.__price = value
    
    price = property(get_price, set_price) # Here we call the built in proprety function


product = Product_2(50)
print(product.price)

# product.price = -10 # If we try to set the price to -1 we wiil raise an execption
# print(product.price)



# but even here we can use a decorator to achive a better looking code

class Product_3:
    def __init__(self, price):
        self.price = price # We change the constructor from "self.price = price" to the set price function

    @property # here we apply the proprety decorator to this method. And renaming the method to the ideal name, in this case price
    def price(self): 
        return self.__price
    
    @price.setter  # Here we also have to add a decorater. The name of the decorater starts with the name of the proprety "price" and the .setter
    def price(self, value): 
        if value < 0:
            raise ValueError("Price can not be negative")
        else:
            self.__price = value


product = Product_3(50)
print(product.price)
product.price = -1 # If we try to set the price to -1 we wiil raise an execption
print(product.price)