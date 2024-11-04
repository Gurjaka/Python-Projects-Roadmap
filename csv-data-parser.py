import csv

file = input('Filename: ')

with open(file, 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)
