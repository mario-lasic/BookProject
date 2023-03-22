from collections import deque

def adding_books(root_node, sub_genre, genre):
    path_queue = deque()

    initial_path = [root_node]

    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]
        if current_node.genre == genre or current_node.genre is None:
            
            if current_node.sub_genre == sub_genre:
                return current_node
        
            for child in current_node.children:
                new_path = current_path[:]
                new_path.append(child)
                path_queue.appendleft(new_path)

    return None

def getting_books(root_node, genre, sub_genre = None):
    path_queue = deque()
    
    initial_path = [root_node]
    path_queue.appendleft(initial_path)

    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]

        if current_node.genre is None:
            for child in current_node.children:
                new_path = current_path[:]
                new_path.append(child)
                path_queue.appendleft(new_path)

        if current_node.genre == genre:
            if sub_genre == None:
                grand_children = []
                for child in current_node.children:
                    for grand_child in child.children:
                        grand_children.append(grand_child)
                return grand_children
            if current_node.sub_genre == sub_genre:
                return current_node.children
            
            for child in current_node.children:
                new_path = current_path[:]
                new_path.append(child)
                path_queue.appendleft(new_path)
