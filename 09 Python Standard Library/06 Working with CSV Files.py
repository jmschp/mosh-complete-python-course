# 06 Working with CSV Files

import csv # first we need to import the csv module

# with open(r"09 Python Standard Library\data.csv", 'w', newline='') as csv_file: # First we create and open the file in the desired location with the "open()" function in the write mode "w'.
#     writer = csv.writer(csv_file)  # The "csv" module as a method for creating a csv writer "csv.writer()". In here we are storeing that method in the "writer" variable.
#     writer.writerow(["transaction_id", "product_id", "price"]) # And now we can write tabular data to our file. Here writing the first row with headings.
#     writer.writerow([1, 48721, 120.00]) # Each row with data
#     writer.writerow([2, 48725, 500.00])


with open(r"09 Python Standard Library\data.csv", "r") as csv_file:
    reader = csv.reader(csv_file)  # The "csv" module as a method for creating a csv reader "csv.reader()". In here we are storeing that method in the "reader" variable.
    print(reader) # The reader returns a iteable object
    # print(list(reader)) # We can call the list function to convert all the info in the csv file to a list. Each line will be a list in the list
    for row in reader: # Because the "reader" is itable we can use a for loop over it.
        print(row)

# We can not iterate twice in "reader" object. Because it has an index and that starts in the beginning of the file.
# And after the first iteration it goes to the end of the file.
# If we iterat ir again  we will not get any readings.