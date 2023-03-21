from tree import TreeNode
import csv
genres = []
sub_genres = {}

with open('books.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["Genre"] not in genres:
            genres.append(row["Genre"])
        list_of_sub = sub_genres.get(row["Genre"])
        if list_of_sub == None:
            key = row["Genre"]
            if sub_genres.get(key) is None:
                sub_genres[key] = []
                sub_genres[key].append(row["SubGenre"])
            else:
                sub_genres[key].append(row["SubGenre"])
        elif row["SubGenre"] not in list_of_sub:
            key = row["Genre"]
            if sub_genres.get(key) is None:
                sub_genres[key] = []
                sub_genres[key].append(row["SubGenre"])
            else:
                sub_genres[key].append(row["SubGenre"])

# Making a tree #

root = TreeNode("root")
for genre in genres:
    current_child = TreeNode(genre, genre, None)
    root.add_child(current_child)
    for sub_genre in sub_genres[genre]:
        grand_child = TreeNode(sub_genre, genre, sub_genre)
        current_child.add_child(grand_child)

#print(genres)
#print(sub_genres.values())
    
