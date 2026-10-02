# heap = [2, 5, 7, 10, 8]
# insert(3)
def insert(self, value):
    self.heap.append(value) # append(3)
    # heap = [2, 5, 7, 10, 8, 3]
    self._heapify_up(len(self.heap) - 1) #_heapify_up(3)
    # _heapify_up = heap length - 1 = 6 - 1 = 5
def _heapify_up(self, i): # i = 5
    while i > 0: # 2 > 0
        # find its parent (3's parent)
        parent = self._parent(i) # i = 2
        # parent = 0
        # 3's parent is at index 0
        if self.heap[i] >= self.heap[parent]:
            # 3 > 2 (true)
            break # break

        self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
        # swap 3 with 7
        # heap = [2, 5, 3, 10, 8, 7]
        i = parent
        # i = 0

#   Final heap: heap = [2, 5, 3, 10, 8, 7]