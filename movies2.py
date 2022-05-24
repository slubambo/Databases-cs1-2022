import csv

with open("gross movies.csv", "r", encoding='UTF8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Film"])
