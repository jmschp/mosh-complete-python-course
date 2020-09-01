# 02 Compiled Python Files

#  __pychache__ it's a folder creates by automaticallyby Pyhton for the compiled files
# In our example we have "sales.cpython-38.pyc"
# The reason Python stores this compile files in this folder is to speed up modlue loading.
# The next time we run our program Python will look at the content of this folder, and if we have a compiled version, Python will simple load that compiled version.
# Skping the compilation of the module. This speeds up the loading of the module, but not its actual performance.
# Python compares the day time of the compiled version with the source code to check if the compiled version is up to date.
# If the day time of the source code is newer it will recompile and store it in teh __pycache__
# The "cpython-38" we see in the compiled file represents the Python implementation used to compile this file.
# In our case it ws compiled using Python 3.8
# In this file we have Python bit code
# Python always recompiles the module we load directly from the comand line.