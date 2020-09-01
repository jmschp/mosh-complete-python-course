# 04 Working with Files

from pathlib import Path
from time import ctime
import shutil

path = Path(r"09 Python Standard Library\test_folder\test_file.py")
print(path.exists())
# path = path.rename(r"09 Python Standard Library\test_folder\test_file2.py") # To rename a direcdtory
print(path.stat()) # With the ".stat()" method we get a "os.stat_result" object with the following attributes
# os.stat_result(st_mode=33206,
#                st_ino=3659174697362956,
#                st_dev=3465398945,
#                st_nlink=1, st_uid=0,
#                st_gid=0,
#                st_size=0, # This returns the size of the file in bytes
#                st_atime=1593375129, # This is the last access time
#                st_mtime=1593375132, # The last modified time
#                st_ctime=1593370616) # The creation time

# This time values are in second after epic. Epic is the start up time on a computer, and that is platform dependent.
# For example on unix systems the epic time is 01/01/1970.
# To print the human readable time we need to import the "ctime" function from the "time" module
print(ctime(path.stat().st_ctime))

path.read_bytes() # which return the content of a file as a bytes object for reprersenting binary data

print(path.read_text()) # Which return the content of the file as a string. Using this method it is easier to read a file that the built-in "open()" function.

file = open(r"09 Python Standard Library\test_folder\test_file.py", "r")
print(file.read())
file.close()

# Or use the "with" statment, as a best practice. Because it will automatacly close the file after it finishes the operation

with open(r"09 Python Standard Library\test_folder\test_file.py", "r") as file:
    print(file.read())

# print(path.write_text('print("Test from lesson 04 Working with Files")'))


# To copy files it is better to impot the shell utilities module "shutil".
# It provides a number of high level operation to copy and move files and directories

target_path = Path(r"09 Python Standard Library") / "test_file.py"

shutil.copy(path, target_path)

target_path.unlink() # To delete a file