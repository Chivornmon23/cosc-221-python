# represents one node
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# represents the whole tree
class BinaryTree:
    def __init__(self):
        self.root = None

class Solution:
    def preorder_traversal(self, node, result):
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)

    def breadth_traversal(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

solver = Solution()

# pre_result = []
# solver.preorder_traversal(tree.root, pre_result)
# print("Preorder:", pre_result)
#
# in_result = []
# solver.inorder_traversal(tree.root, in_result)
# print("Inorder: ", in_result)
#
# post_result = []
# solver.postorder_traversal(tree.root, post_result)
# print("Postorder:", post_result)
#
# breadth_result = solver.breadth_traversal(tree.root)
# print("Breadth_result: ", breadth_result)
