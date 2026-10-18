class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_link = Node(value)
        if not self.root:
            self.root = Node(value)
        else:
            curr = self.root
            while True:
                if value < curr.value:
                    if not curr.left:
                        curr.left = new_link
                        break
                    curr = curr.left
                else:
                    if not curr.right:
                        curr.right = new_link
                        break
                    curr = curr.right
    def in_order(self, node, result = None):
        if result is None:
            result = []
        if node:
            self.in_order(node.left, result)
            result.append(node.value)
            self.in_order(node.right, result)
        return result

tree = BinaryTree()
key = [20, 10, 50, 40, 60, 30]

for k in key:
    tree.insert(k)

print("Inorder Traversal: ", tree.in_order(tree.root))
print("This outputs the nodes of a binary tree in ascending order.")