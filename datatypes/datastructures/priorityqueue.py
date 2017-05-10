from time import time

# Using lists
now = time()
q = []

q.append((2, 'code'))
q.append((1, 'eat'))
q.append((3, 'sleep'))

# NOTE: Remember to re-sort every time
#       a new element is inserted, or use
#       bisect.insort().
q.sort(reverse=True)

while q:
    next_item = q.pop()
    done = time()
    print(next_item, (done-now)*1000)

# Result:
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')

# Using heapq python module

import heapq
now1 = time()
q = []

heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))

while q:
    next_item = heapq.heappop(q)
    done = time()
    print(next_item, (done-now)*1000)

# Result:
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')

# Using PriorityQueue Class

from queue import PriorityQueue

q = PriorityQueue()

q.put((2, 'code'))
q.put((1, 'eat'))
q.put((3, 'sleep'))

while not q.empty():
    next_item = q.get()
    print(next_item)

# Result:
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')
