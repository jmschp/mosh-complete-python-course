# 04 Packages

# As our application grows we are going to organize it in folder. Separating the modules in folders for a better organization.
# Here we created a folder "ecommerce" and put the "esales.py" module there.
# We have to add a "__init__.py" file to the "ecommerce" folder, When we do that Python treats that folder as a Package.
# A Package is a countainer for one or more modules.
# In file sytems terms a [Pakages] is mapped to a [directory] and a [module] is mapped to a [file].

import ecommerce.esales # To import the "esales.py" module we have to prefix it with the name of the package.

ecommerce.esales.calc_tax() # to use any of the function in the "esales.py" module we have to prefix it with the nam,e fo the package.

from ecommerce.esales import calc_tax, calc_shipping # This way is better because we don't need to prefix the name of the package everytime we want to use a function

calc_shipping()
calc_tax()

from ecommerce import esales # If we have to import a lot a functions and it becomes noisy in the above method. We can import it like this.

esales.calc_shipping() # And just use "esales" with the "." operator to access the functions in that module.
esales.calc_tax()