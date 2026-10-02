# heap = [2, 5, 7, 10, 8, 12, 15]
# we take the last value and move it to the root
# index = 0  1  2  3  4  5
# heap = [15, 5, 7, 10, 8, 12]
#           15
#          /   \
#         5     7
#        /  \   /
#       10   8  12

# heapify_down(0)
def _heapify_down(self, i):
    while True:
        # left = 2(0) + 1 = 1 ; 3
        # right = 2(0) + 2 = 2 ; 4
        left = self._left(i) # left = 1
        right = self._right(i) # right = 2

        smallest = i # smallest = 0 (we assume the current node is the smallest)
        # 2nd: smallest = 1

        # Does the left child actually exist?   and Is the left child smaller than what I currently think is the smallest
        # 1 < 6 and 5 < 15
        # 2nd: 3 < 6 and 10 < 15 (true)
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left # smallest = 1 ; smallest = 3

        # Does the right child currently exist? and Is the right child smaller than what I currently think is the smallest
        # 2 < 6 and 7 < 5 (false)
        #                   smallest = 1 (remains)
        # 4 < 6 and 8 < 10 (true)

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
            # smallest = 4
        # Is the current node alr the smallest compared with its children?
        if smallest == i: #smallest == i = 1 == 0 (false) ; 4 == 1
            break

        # If not, we need to swap
        self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
        # 15, 5
        # 5, 15

        # 15, 8
        # 8, 15
        i = smallest # i = 1 ; i = 4

        # 1st iteration: final heap: heap = [5, 15, 7, 10, 8, 12]
        #         5
        #        / \
        #       15   7
        #      / \  /
        #     10 8 12

        # 2nd iteration: second heap: [5, 8, 7, 10, 15, 12]
        #         5
        #        / \
        #       8   7
        #      / \
        #     10 15