## Users CSV file

import csv

fields = [
    ['username', 'password']
]

data = [
    ['admin','Admin@123'],
    ['student','Student@123']
]

#File Path for creating / writing CSV files
file_path = 'users.csv'

# Writing Data into the CSV file

with open(file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(fields)
    writer.writerows(data)