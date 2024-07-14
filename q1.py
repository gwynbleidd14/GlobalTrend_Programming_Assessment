'''
1. Implement a Python class MaxHeap that supports the following operations: insert,
delete, and get_max. Ensure the operations maintain the properties of a max-heap.
'''

import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self, value):
        heapq.heappush(self.heap, -value)
    
    def delete(self):
        return -heapq.heappop(self.heap)
    
    def get_max(self):
        if self.heap:
            return -self.heap[0]
        else:
            return None
    
    def __len__(self):
        return len(self.heap)
    
max_heap = MaxHeap()
l = int(input("Enter number of elements: "))
for i in range(1, l + 1):
    print("Enter number", i)
    n = int(input())
    max_heap.insert(n)

print("Maximum:",max_heap.get_max())

print("Max heap elements:")
while len(max_heap) > 0:
    print(max_heap.delete())
