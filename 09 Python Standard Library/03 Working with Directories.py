# 03 Working with Directories

from pathlib import Path


path = Path(r"09 Python Standard Library\test_folder2")
print(path.exists())
# path.mkdir() # To create a directory
# path = path.rename(r"09 Python Standard Library\test_folder3") # To rename a direcdtory
# path.rmdir() # To remove a directory

path = Path(r"09 Python Standard Library")
print(path.iterdir()) # With this method we can gel the list of files and directories. This returns a genarator object.
# Because we may be working with a large list of item. Instead of storing all tho item in the memory, We use a genarator object.
# Each time we itarate over it we willl get a new item.

for p in path.iterdir(): # With the for loop we can iterate over the genarator. and get each file and folder
    print(p)


paths = [p for p in path.iterdir()] # If we are not working with a large list of file and folders we can use a list comprehension, to store all the values in a list.
print(paths)

filter_directories = [p for p in path.iterdir() if p.is_dir()] # If we want to create a list with only the directories.
print(filter_directories)

filter_files = [p for p in path.iterdir() if p.is_file()] # If we want to filter the files.
print(filter_files)

# the ".iterdir()" has two limitations.
# 1. We can not search by a pattern.
# 2. It does not search recursively.
# To over come this we can use the ".glob()" method. This also retruns a genarator
# To search recursively we can use the ".rglob()".

print(path.glob("*.*")) # to search for all file
print(path.glob("*.py")) # to search for file with the extension ".py"

py_files = [p for p in path.glob("*.py")]
print(py_files)

py_files = [p for p in path.rglob("*.py")] # we will get all the py files in this folder and sub folders.
print(py_files)
