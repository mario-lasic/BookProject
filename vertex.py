class Vertex:
    def __init__(self, value, genre, sub_genre) -> None:
        self.value = value
        self.genre = genre()
        self.sub_genre = sub_genre
        self.edges = {}

    def get_edges(self):
        return list[self.edges.keys()]
        
    def add_edge(self, vertex):
        self.edges[vertex] = True
