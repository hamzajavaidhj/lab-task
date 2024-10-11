class Node:
    def __init__(self, position, parent=None):
        self.position = position  
        self.parent = parent  
        self.g = 0       
        self.h = 0                
        self.f = 0                
    def __eq__(self, other):
        return self.position == other.position
def heuristic(node_position, goal_position):
    return abs(node_position[0] - goal_position[0]) + abs(node_position[1] - goal_position[1])
def a_star(start, goal, grid):
    open_list = []
    closed_list = [] 
    start_node = Node(start)
    goal_node = Node(goal)
    open_list.append(start_node)
    while open_list:
        open_list.sort(key=lambda x: x.f)
        current_node = open_list.pop(0)
        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        closed_list.append(current_node)
        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)] 
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (len(grid) - 1) or node_position[0] < 0 or node_position[1] > (len(grid[len(grid) - 1]) - 1) or node_position[1] < 0:
                continue    
            if grid[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(node_position, current_node)
            if new_node in closed_list:
                continue
            new_node.g = current_node.g + 1
            new_node.h = heuristic(new_node.position, goal_node.position)
            new_node.f = new_node.g + new_node.h
            if add_to_open(open_list, new_node):
                open_list.append(new_node)
    return None
def add_to_open(open_list, neighbor):
    for node in open_list:
        if neighbor == node and neighbor.g >= node.g:
            return False
    return True
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  
goal = (4, 4)  
path = a_star(start, goal, grid)
if path:
    print("Path is found:", path)
else:
    print("No Path is found.")