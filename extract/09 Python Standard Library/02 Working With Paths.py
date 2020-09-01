# 02 Working With Paths

# The path class is the fondation to work with files an directories.
# https://docs.python.org/3/library/pathlib.html

from pathlib import Path # importing from the "pathlib" modle the "Path" class.

path = Path("C:\\Users\\jmigu\\Desktop") # creating a path object in Windows.
path = Path(r"C:\Users\jmigu\Desktop") # we can also do it with a raw string using the "r" in the begining. In a raw string the "\" it is not an escape sequence.

path_current_folder = Path() # To creat a path object that represents the current folder.

relative_path = Path(r"09 Python Standard Library\test_folder\test_file.py") # A relative path. In the curretn folder go to the subfolder "test_folder".

combine_path = Path(r"C:\Users\jmigu\Desktop") / Path(r"test_folder") # We can use the "/" to combine path obejects.
combine_path = Path(r"C:\Users\jmigu\Desktop") / "new folder" # We can use the "/" to combine path with a string.
print(combine_path)

print(Path.home()) # The home method returns the home directory of the current user.

print(relative_path.exists()) # Call the ".exist()" to see if a file or directory exists. Return a boolean value.

print(relative_path.is_file()) # To check if this path represent a file.
print(relative_path.is_dir()) # To check if this path represent a directory.
print(relative_path.name) # this return only the file name in this path.
print(relative_path.stem) # this returns the file name without the extension.
print(relative_path.suffix) # This return only the extension of the file.
print(relative_path.parent) # This return the parent folders.
print(relative_path.with_suffix(".txt")) # To change the extension of the file

new_path = relative_path.with_name("file.txt") # This creates a new path object based in th existin path nut changes the name and extension of the file.
print(new_path)


print(relative_path.absolute()) # To get the absolute path.

relative_path.with_suffix(".txt")