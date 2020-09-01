# 08 Working with a SQLite Database

import sqlite3
import json
from pathlib import Path

# We are going to read all the movies from the JSON file from the last leson and store then in a data base

movies = json.loads(Path(r"09 Python Standard Library\movies.json").read_text())

#with sqlite3.connect(r"09 Python Standard Library\movies_db.db") as connection: # The ".connect()" method from the "sqlite3" module returns a connection object.
    # We pass to it the name of our data base. If it does not exist, it will create it.
#    command = "INSERT INTO Movies VALUES(?, ?, ?)" # First we need to create a command for the data base, this is SQL languge each "?" is a placemark for our value.
#    for movie in movies:
#        connection.execute(command, tuple(movie.values())) # We are lopping over over our JSON file store in our variable "movies". And executing the "command", in the values for each movie, that have to be converted as tuples.
#    connection.commit() # When we are done we should call the ".commit()" method that will write all the changes to the data base.


# Now we are going to read the from our data base

with sqlite3.connect(r"09 Python Standard Library\movies_db.db") as connection:
    command = "SELECT * FROM Movies" # We write the command. In this case "SELECT * FROM Movies" to read all the movies from the "Movies" Table
    cursor = connection.execute(command) # When we read data from a data base this returns a cursor. A cursor is an iterable object.
    #for row in cursor:
    #    print(row) # for each iteration we get a tuple with the content of each row.
    movies = cursor.fetchall() # With this method we will get a list with all the rows. We can not run it after the for loop, because the cursor will ben in the end of the rowes, and it will not retunr any values.
    print(movies)