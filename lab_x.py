import os
import csv
import json


csv_folder = '~/Desktop/csv_data/'

all_data = []

for filename in os.listdir(csv_folder):
    if filename.endswith('.csv'):
    
        with open(os.path.join(csv_folder, filename), 'r') as csvfile:
         
            csv_data = csv.DictReader(csvfile)
    
            for row in csv_data:
              
                all_data.append(row)

# Write the data to a JSON file
with open('output.json', 'w') as outfile:
    json.dump(all_data, outfile)