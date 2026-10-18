class Link:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init(self):
        self.root = None

    def insert(self, value):
        new_link = Link(value)
        if not self.root:
            self.root = new_link
        else:
            current = self.root
            while True:
                if value < current.value:
                    if not current.left:
                        current.left = new_link
                        break
                    current = current.left
                else:
                    if not current.right:
                        current.right = new_link
                        break
                    current = current.right
    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False
    def get_height(self, node):
        if not node:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return max(left_height, right_height) + 1
tree = BinaryTree()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    tree.insert(v)

print(tree.search(40))
print(tree.search(90))
print(tree.get_height(tree.root))