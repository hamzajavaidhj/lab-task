#  Task 1
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child_node):
        self.children.append(child_node)
def dfs_with_stack(root):
    stack = [root]
    visited = []
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            print(current_node.value)
            stack.extend(reversed(current_node.children))
if __name__ == "__main__":
    root = Node(1)
    child1 = Node(2)
    child2 = Node(3)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(4))
    child1.add_child(Node(5))
    child2.add_child(Node(6))
    dfs_with_stack(root)

# Task 2

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def inorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            result.append(node.value)
            dfs(node.right)
    dfs(root)
    return result

def preorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            result.append(node.value)
            dfs(node.left)
            dfs(node.right)
    dfs(root)
    return result

def postorder_traversal(root):
    result = []
    def dfs(node):
        if node:
            dfs(node.left)
            dfs(node.right)
            result.append(node.value)
    dfs(root)
    return result

