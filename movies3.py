import csv

films = set()

with open("gross movies.csv", "r", encoding='UTF8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        films.add(row["Film"].strip().upper())

    for film in sorted(films):
        print(film)
