class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

#Pointer manipulation
curr = head # (1) curr = 10 (2) curr = 20 (3) curr = 30
while curr.next and curr.next.next: # (1) 20 and 30 (2) 30 and 40 (3) 40 and None
    curr = curr.next # (1) curr = 20 (2) curr = 30
curr.next = None # curr.next = None (30.next = None)

out = []
curr = head # 10
while curr: # (1) 10, (2) 20, (3) 30, (4) curr = None false
    out.append(curr.val) # [10, 20, 30]
    curr = curr.next # curr = 20, 30, None
print(out) # [10, 20, 30]