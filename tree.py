class TreeNode:

    def __init__(self, value = None, genre = None, sub_genre = None) -> None:
        self.value = value
        self.genre = genre
        self.sub_genre = sub_genre
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse(self):
        nodes_to_visit = [self]
        while nodes_to_visit > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            current_node += current_node.children