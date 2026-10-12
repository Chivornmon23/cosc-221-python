class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root is not None:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

# Example usage
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(3)
root.left.right = Node(7)

print("Pre Order Traversal: ", end=" ")
preorder(root)