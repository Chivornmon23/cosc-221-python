class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

first = Node("A")
second = Node("B")
first.next = second
head = first 

print(head.value)
print(head.next.value)
print(head.next.next is None)

current = head 
while current is not None:
    print(current.value)
    current = current.next