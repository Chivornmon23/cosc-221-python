def postorder_traversal(self, node, result):
    if node:
        self.postorder_traversal(node.left, result) #1. Traverse left
        self.postorder_traversal(node.right, result)    #2. Traverse Right
        result.append(node.value)   #3. Visit root
        
