class Link:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        new_link = Link(value)
        if self.root is None:
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
    def pre_order(self, node, result = None):
        if result is None:
            result = []
        if node:
            result.append(node.value)
            self.pre_order(node.left, result)
            self.pre_order(node.right, result)
        return result
    def post_order(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.post_order(node.left, result = None)
            self.post_order(node.right, result)
            result.append(node.value)
        return result
    def in_order(self, node, result = None):
        if result is None:
            result = []
        if node:
            self.in_order(node.left, result)
            result.append(node.value)
            self.in_order(node.right, result)
        return result
    def level_order(self):
        if not self.root: #check for an empty tree
            return [] # return empty list
        result = [] # to store the final visited order
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def display(self):
        print("Pre-order: ", self.pre_order(self.root))
        print("In-order:", self.in_order(self.root))
        print("Post-order:", self.post_order(self.root))
        print("Level-order:", self.level_order())

tree = BinaryTree()
values = [50, 30, 70, 20, 40, 60, 80]
for v in values:
    tree.insert(v)

tree.display()

