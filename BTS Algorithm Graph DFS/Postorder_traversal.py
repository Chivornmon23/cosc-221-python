class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

# Example usage
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(3)
root.left.right = Node(7)

print("Post Order Traversal: ", end=" ")
postorder(root)