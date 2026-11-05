from Tree_traversal import Solution

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node (value)
            else:
                self._insert_recursive(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

tree = BinaryTree()

values = [10, 5, 20, 3, 7, 25]
for val in values:
    tree.insert(val)

solver = Solution()
result = []
solver.preorder_traversal(tree.root, result)
print("Pre: ", result)

in_result = []
solver.inorder_traversal(tree.root, in_result)
print("Inorder: ", in_result)

post_result = []
solver.postorder_traversal(tree.root, post_result)
print("Postorder:", post_result)

breadth_result = solver.breadth_traversal(tree.root)
print("Breadth_result: ", breadth_result)