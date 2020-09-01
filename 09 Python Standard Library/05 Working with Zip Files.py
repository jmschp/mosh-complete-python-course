# 05 Working with Zip Files

from pathlib import Path
from zipfile import ZipFile
import shutil

# first we creat a zip objec

with ZipFile("files.zip", mode="w") as zip_file: # With the "with" statmente we create the zip file "files.zip" as an object "zip_file". With the write mode "w", to write to taht file.
    path = Path(r"09 Python Standard Library") # Here we determine the files we want 
    for p in path.rglob("*.*"): # We itarete ober each file and folder. 
        zip_file.write(p) # and write it to the zip file


with ZipFile("files.zip", mode="r") as zip_file: # Here we open the file in read mode.
    print(zip_file.namelist()) # With the ".nameList()" method we can return a list of all the files in the zip file.
    info = zip_file.getinfo('09 Python Standard Library/02 Working With Paths.py') # This returns a info object.
    print(info)
    print(info.file_size) # To get the file size
    print(info.compress_size) # to get the compress file size
    zip_file.extractall("extract") # To extract all the file in the zip file to a directory, in our case we created the directory "extract"