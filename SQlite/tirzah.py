import csv

from cs50 import SQL

open("flicks.db", "w").close()

db = SQL("sqlite:///flicks.db")

db.execute("CREATE TABLE movies (id INTEGER, title TEXT, PRIMARY KEY(id))")

db.execute("CREATE TABLE genres (movie_id INTEGER, genre TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id))")

with open("gross movies.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:

        title = row["Film"].strip().capitalize()

        db.execute("INSERT INTO movies VALUES(?)", title)

        