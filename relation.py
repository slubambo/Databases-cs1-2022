import csv

from cs50 import SQL

open("gross_movies_db.db", "w").close()

db = SQL("sqlite:///gross_movies_db.db")

db.execute("CREATE TABLE movies (id INTEGER, title TEXT, PRIMARY KEY(id))")

db.execute("CREATE TABLE genre (movie_id INTEGER, genre TEXT, FOREIGN KEY(movie_id) REFERENCES movies(id))" )

with open("gross movies.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["Film"].strip().capitalize()

        id = db.execute("INSERT INTO movies (title) VALUES(?)", title)

        for genre in row["Genre"].split(","):

            db.execute("INSERT INTO genre (movie_id, genre) VALUES (?,?)", id, genre)
