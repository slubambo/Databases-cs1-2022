import csv

title = input("Title: ")

with open("gross movies.csv", "r", encoding='UTF8') as file:
    reader = csv.DictReader(file)

    counter = 0

    for row in reader:
        if row["Film"].strip == title:
            counter += 1

    print(counter)
