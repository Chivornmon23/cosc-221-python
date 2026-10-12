class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None: # 20
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    if target < root.value:
        return search(root.left, target)
    else:
        return search(root.right, target)

root = None
items = [45, 25, 60, 10, 30, 55, 70, 5, 20, 35]

for item in items:
    root = insert(root, item)

print("BST root: ", root.value)
print("Left child: ", root.left.value)
print("Right child: ", root.right.value)
print("Left-right child: ", root.right.left.value)

result = search(root, 20)
print("Does 20 exist? ", result)

