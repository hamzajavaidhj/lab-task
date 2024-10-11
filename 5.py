class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    def dfs_stack(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
    def preorder(self, node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)
if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.dfs_stack()
    tree.inorder(tree.root)
    tree.preorder(tree.root)
    tree.postorder(tree.root)
