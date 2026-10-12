class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

root = None
items = [45, 25, 60, 10, 30, 55, 70, 5, 20, 35]

for item in items:
    root = insert(root, item)

print("Inorder Traversal: ", end=" ")
inorder(root)


newItems = [168, 27, 20]
for newItem in newItems:
    root = insert(root, newItem)
print()
print("Inorder Traversal: ", end=" ")
inorder(root)