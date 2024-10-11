# Task 1

def bfs(graph, start):
    visited = set()
    visited.add(start)
    result = [start]
    
    while result:
        node = result.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                result.append(neighbor)
    print(visited)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(bfs(graph, 'A'))

# Task 2
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
def bfs(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current.value)        
        for child in current.children:
            queue.append(child) 
    return result
if __name__ == "__main__":
    root = Node(1)
    root.children = [Node(2), Node(3)]
    root.children[0].children = [Node(4), Node(5)]
    root.children[1].children = [Node(6)]
    print(bfs(root))
