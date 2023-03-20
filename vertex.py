class Vertex:
    def __init__(self, value, type) -> None:
        self.value = value
        self.type = type[:2].lower()
        self.edges = {}

    def get_edges(self):
        return list[self.edges.keys()]
        
    def add_edge(self, vertex):
        self.edges[vertex] = True
