import os
import csv
import json

# Set the directory path where the CSV files are located
directory_path = ""D:\sem4\Data modelling\lab_x""

# Loop through each file in the directory
for filename in os.listdir(directory_path):
    # Check if the file is a CSV file
    if filename.endswith(".csv"):
        # Open the file and read its contents
        with open(os.path.join(directory_path, filename), "r") as f:
            # Read the contents of the CSV file using the csv.reader() function
            reader = csv.reader(f)
            # Get the header row of the CSV file
            header = next(reader)
            # Create an empty list to hold the rows of data
            data = []
            # Loop through each row of the CSV file and append it to the data list
            for row in reader:
                data.append(row)
        # Create a dictionary from the header row and the data rows
        dict_list = [dict(zip(header, row)) for row in data]
        # Convert the dictionary to JSON and write it to a file
        with open(os.path.splitext(filename)[0] + ".json", "w") as json_file:
            json.dump(dict_list, json_file)