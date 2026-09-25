# A Priority Queues is an abstract data type (ADT) that stores elements 
# along with their priorities. Unlike a regular queue (FIFO), a priority queue 
# removes elements based on their priority, not their insertion order.

# important operation 
# 1. add(k,v): inserts an item with key k and value v
# 2. min(): returns the item(k, v) with the smallest key without removing it
# 3. remove_min(): removes and returns the item (k,v) with the smallest key

# Practice: 
# Simulate a queue of people waiting for a service (like at a bank). 
# Each person arrives at the bank and waits for their turn to be served.
# modify the program to include priority. For example, VIP customers should be served first

class Queue:
    def __init__(self):
        self.normal_queue = []
        self.vip_queue = []
    
    def enqueue(self, person, is_vip=False):
        """Add person to the VIP or normal queue based on priority"""
        if is_vip:
            self.vip_queue.append(person)
        else:
            self.normal_queue.append(person)
    
    def dequeue(self):
        """Serve the first person from the VIP queue, if available, else from the normal queue"""
        if self.vip_queue:
            return self.vip_queue.pop(0)
        elif self.normal_queue:
            return self.normal_queue.pop(0)
        return "Queue is empty"
    
    def first(self):
        """Return the first person in the VIP queue or normal queue"""
        if self.vip_queue:
            return self.vip_queue[0]
        elif self.normal_queue:
            return self.normal_queue[0]
        return "Queue is empty"

# Simulate the queue with priority
queue = Queue()

queue.enqueue("Tena")  # Alice is VIP
queue.enqueue("pitu")
queue.enqueue("Vannda", is_vip=True)  # Charlie is VIP

# Serve the first person
print(f"Served: {queue.dequeue()}")  # Alice (VIP)
print(f"Next in line: {queue.first()}")  # Charlie (VIP)