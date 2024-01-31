import csv

results = []

file_path = 'results.csv'

with open(file_path, 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Results'])

    for result in results:
        writer.writerow([result])

print(f"Your result has been stored in '{file_path}' CSV file successfully!")