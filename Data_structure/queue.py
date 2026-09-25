# A queue is a collection of objects that are inserted and removed
#  according to the first-in, first-out (FIFO) principle.

# Important operation 
# 1. Q.enqueue(e): add element e to the back of the queue Q.
# 2. Q.dequeue(): remove and return the first element from the queue Q. 
# 3. Q.first(): return a reference to the element at the front of queue Q, without removing it

#Problem 1: Simulate a queue of people waiting for a service (like at a bank). 
# Each person arrives at the bank and waits for their turn to be served.

class Queue:
    def __init__(self): #is a special method in Python classes, commonly known as a constructor.
        self.queue = []

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0
    
    def enqueue(self, person):
        """Add person to the back of the queue"""
        self.queue.append(person)

    def dequeue(self):
        """Remove and return the first person in the queue"""
        if self.is_empty():
            return "No one is in the queue"
        return self.queue.pop(0)
    
    def first(self):
        """Return the first person in the queue without removing"""
        if self.is_empty():
            return "No one is in the queue"
        return self.queue[0]

# Simulation
queue = Queue()

# Adding people to the queue
queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")

# Checking the first person in the queue
print(f"First in line: {queue.first()}")  # Output: Alice

# Serving the first person
served_person = queue.dequeue()
print(f"Served: {served_person}")  # Output: Alice

# Checking who is next
print(f"Next in line: {queue.first()}")  # Output: Bob




