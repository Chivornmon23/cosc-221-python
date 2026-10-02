# Min-Heap Array Representation (Lecture-Code/Heap.py)
class MinHeap:
    def __init__(self):
        self.heap = []  # 1D list storing the tree

    # 1. Parent Index: (i - 1) // 2
    def _parent(self, i):
        return (i - 1) // 2 # the mathematical form (trick) that lets an array
        #   find the parent of a node.

    # 2. Left Child Index: 2 * i + 1 
    def _left(self, i):
        return 2 * i + 1

    # 3. Right Child Index: 2 * i + 2
    def _right(self, i):
        return 2 * i + 2

    # 4. O(1) Minimum Lookup (Root is always at [0])
    def peek(self):
        return self.heap[0] if self.heap else None
