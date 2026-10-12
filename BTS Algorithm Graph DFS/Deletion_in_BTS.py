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

def delete(root, value):
    if root is None:
        return None

    if value < root.value:
        root.left = delete(root.left, value)

    elif value > root.value:
        root.right = delete(root.right, value)

    else:
        # Case 1 and Case 2
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        # Case 3: Two children (Deleting a node with two children)
        successor = root.right

        while successor.left is not None:
            successor = successor.left

        root.value = successor.value
        root.right = delete(root.right, successor.value)

    return root

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

print()
print("Delete 10 and 168 and 20: ")
delete(root, 10)
delete(root, 168)
delete(root, 20)
inorder(root)