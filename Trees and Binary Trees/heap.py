import heapq

heap = [2, 5, 8, 10]
heapq.heapify(heap)

heapq.heappush(heap, 1)
print(heap)
print(heapq.heappop(heap))