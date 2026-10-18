from collections import deque

q = deque()
if q:
    item = q.popleft()
else:
    print("Queue is empty")

print(q)