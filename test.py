import csv

readFile = []

with open('data.csv', 'r') as file:

    csv1 = csv.reader(file)

    for item in csv1:
        print(item)

