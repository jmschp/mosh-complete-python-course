# 17 Running External Programs

# Let's we want our Python program to run the "dir" comand and capture the output.
# We can run other programs othe execute another python script.

import subprocess
from pathlib import Path
# We need to import the "subprocess" module. With this module we can span a child process. A process is basicly an instance of a running program. so with this module we can run other programs.

completed = subprocess.run(["dir"],
                            shell=True,
                            capture_output=True,
                            text=True) # The first argumente to the ".run()" is an array of strings, that will be the command. In Windows OS we shoulf set shell to true
# If we set "capture_output=True" the output will not be printed on the terminal, instead it will be available in the ".stdout" atribute.
# Tf we set "text=True" the output will be converted from a binary to string. And we can sve it to a file.
print(type(completed))
print("Args: ", completed.args)
print("Return code: ", completed.returncode)
print("Standard error: ", completed.stderr)
print("Standard output", completed.stdout)



# Now in another example we are going to run another Python script - other.py

completed = subprocess.run(["python", Path(r"09 Python Standard Library\other.py")],
                            shell=True,
                            capture_output=True,
                            text=True)
print("Args: ", completed.args)
print("Return code: ", completed.returncode)
print("Standard error: ", completed.stderr)
print("Standard output", completed.stdout)

# We are execution this other Python script as a child process.
# So it will be in a completely different memory space.
# This is different from importing that script and executing it here.
# This two script will be in two different process and will not share the same variables.


# Here we will use the command "false" to force an error. So we can place the code in a "try block".

try:
    completed = subprocess.run(["false"],
                                shell=True,
                                capture_output=True,
                                text=True,
                                check=True)
                                # If we set "check=True" this will raise an exception
    print("Args: ", completed.args)
    print("Return code: ", completed.returncode)
    print("Standard error: ", completed.stderr)
    print("Standard output", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)