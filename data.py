from vertex import Vertex
from graph import Graph

types = ["Romance", "Classic", "Fantasy", "Poetry", "Comic", "Mystery", "Horror"]

books = Graph(True)

for type in types:
    books.add_vertex(Vertex(type, type))

print(books.graph_dict["Fantasy"].type)

books_vertices = []