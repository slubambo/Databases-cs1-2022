import csv

films = dict()  # or {}

with open("gross movies.csv", "r", encoding='UTF8') as file:
    reader = csv.DictReader(file)

    for row in reader:

        film = row["Film"].strip().upper()

        if film in films:
                films[film] += 1
        else:
                films[film] = 1

    def f(film):
        return films[film]

    for film in sorted(films, key=f, reverse=True):
        print(film, films[film])
