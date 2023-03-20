from vertex import Vertex
from graph import Graph
import csv
genres = []
sub_genre = {}
books = Graph(True)

with open('books.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Genre"] not in genres:
            genres.append(row["Genre"])
        list_of_sub = sub_genre.get(row["Genre"])
        if list_of_sub == None:
            key = row["Genre"]
            if sub_genre.get(key) is None:
                sub_genre[key] = []
                sub_genre[key].append(row["SubGenre"])
            else:
                sub_genre[key].append(row["SubGenre"])
        elif row["SubGenre"] not in list_of_sub:
            key = row["Genre"]
            if sub_genre.get(key) is None:
                sub_genre[key] = []
                sub_genre[key].append(row["SubGenre"])
            else:
                sub_genre[key].append(row["SubGenre"])
        

#print(genres)
print(sub_genre.values())
    
