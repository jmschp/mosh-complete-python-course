# 09 Docstrings

# https://www.python.org/dev/peps/pep-0257/

# When publish our packages it is very important that we documnent tehm well for othr people to use them.
# In this example lets say we have a class with functions o convert PDF to text
# In python we have a special format to documnt our code called "Docstring", that use triple quotes """

""" Module to convert PDF to text. """ # This is an example of a Docstring in the first line of the module.

class Converter:
    """ Asimples converter form converting PDF to text"""
    def convert(self, path):
        """
        Convert a Givenb PDF to text.

        Parameters:
        path (str): The path to a PDF file.

        Returns:
        str: The contect of the PDF file as text.
        """
        print("PDF converted to text")