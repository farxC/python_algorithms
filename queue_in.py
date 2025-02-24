from queue import Queue
from collections import deque

q = Queue()
q.put(1)
q.put(2)
q.put(3)

print(q.get()) # Output: 1
print(q.get()) # Output: 2 
print(q.get()) # Output: 3 
