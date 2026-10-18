class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
    def display(self):
        current = self.head
        out = []

        while current:
            out.append(current.value)
            current = current.next
        print(out)


my_linkedList = LinkedList()

nodes = [20, 30, 40, 50, 60]

for n in nodes:
    my_linkedList.append(n)

print(" ")
my_linkedList.display()