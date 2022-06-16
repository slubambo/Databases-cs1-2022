import csv

from cs50 import SQL

open("films.db", "w").close() #Creating file and closing it or touch in cmd

db = SQL("sqlite:///films.db")

db.execute("CREATE TABLE flicks (id INTEGER, title TEXT, PRIMARY KEY(id))")

db.execute("CREATE TABLE genres (flick_id INTEGER, genre TEXT, FOREIGN KEY(flick_id) REFERENCES flicks(id))")

with open("gross movies.csv",  "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        title = row["Film"].strip().capitalize()

        id = db.execute("INSERT INTO flicks (title) VALUES(?)", title)

        for genre in row["Genre"].split(", "):
            db.execute("INSERT INTO genres (flick_id, genre) VALUES (?,?)" , id, genre)

