# 07 Working with JSON Files

import json
from pathlib import Path

# JSON stands fro JavaScript Object Notation.
# It is a popular way to format data in a huma reable way. A lot of popular of websites provide their data in JSON format.


# The first part of the lesson is about writing data formated as JSON to a file.

movies_write = [
    {"id": 1, "title": "Terminator", "year": 1989}, 
    {"id": 2, "title": "Kindergarten Cop", "year": 1990}]

# First we set an array. In this case an array of movie objects.

data_write = (json.dumps(movies_write)) # With the ".dumps()" method form the "json" module. We convert our object to a string formated as JSON.
print(data_write) # Because we are worjing with Python it will look the same as the syntax we wrote in our "movies" variable.

Path(r"09 Python Standard Library\movies.json").write_text(data_write)

# with open(r"09 Python Standard Library\movies.json", "w") as movies_json: # Or we could use the "with" statment intead od the "Path().write_text".
    # movies_json.write(data)


# In the second part we are going to read teh data from the JSON file.

data_read = Path(r"09 Python Standard Library\movies.json").read_text() # First we read the content of the JSON file and store it in a variable.
# So "data_read" is a string that inclues data formated as JSON.
print(data_read)

movies_read = json.loads(data_read) # Now we parse this string into an array of objects.
print(movies_read) # So movies read becomes a array of dictionaries, that we can access.
print(movies_read[0])