import csv

with open("gross movies.csv", "r", encoding='UTF8') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        print(row[1])
s