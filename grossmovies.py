import csv

movies = {}

with open("gross movies.csv", "r", encoding='UTF8') as file:

    reader = csv.reader(file)
    next(reader)
    
    count = 0;

    for row in sorted(reader):
        title = row[0].strip().lower()
        
        if title in movies:
           
           movies[title] += 1
           
        else:
           movies[title] = 1
    
    def findValue(title):
        return movies[title]
        
    for row in sorted(movies, key= findValue, reverse= True ):
        print(row, findValue(row))
        
        


