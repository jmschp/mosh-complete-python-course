# 06 Intra-package References

#for intra packages reference there two ways to import a package.
# Relative and Absolut

# Supposing we were working on our "eshopping.py" and need to import a function from "contact.py"

from ecommerce.costumer import contact # This is the absolute import

contact.contact_costumer()



from .ecommerce.costumer import contact # We use the "." operator to navigate to the parent folders.
# "one dot ." navigate to the current folder

contact.contact_costumer()

# As a best practice prefer to use the absolute import. Thats waht PEP 8 recommends.