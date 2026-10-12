class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def inorder(root):
    if root is not None:
        inorder(root.left) # Visit the subtree
        print(root.value, end=" ") #process the node (e.g., print)
        inorder(root.right) # Visit right subtree

# Example usage
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(3)
root.left.right = Node(7)

print("Inorder Traversal: ", end="")
inorder(root)


