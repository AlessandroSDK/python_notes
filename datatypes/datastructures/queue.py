# It’s possible to use a regular list as a queue but this is not ideal from a performance perspective. 

# How to use Python's list as a FIFO queue:

q = []

q.append('eat')
q.append('sleep')
q.append('code')

>>> q
['eat', 'sleep', 'code']

# Careful: This is slow!
>>> q.pop(0)
'eat'

# How to use collections.deque as a FIFO queue:

from collections import deque
q = deque()

q.append('eat')
q.append('sleep')
q.append('code')

>>> q
deque(['eat', 'sleep', 'code'])

>>> q.popleft()
'eat'
>>> q.popleft()
'sleep'
>>> q.popleft()
'code'

>>> q.popleft()
IndexError: "pop from an empty deque"

i# How to use queue.Queue as a FIFO queue:

from queue import Queue
q = Queue()

q.put('eat')
q.put('sleep')
q.put('code')

>>> q
<queue.Queue object at 0x1070f5b38>

>>> q.get()
'eat'
>>> q.get()
'sleep'
>>> q.get()
'code'

>>> q.get_nowait()
queue.Empty

>>> q.get()
# Blocks / waits forever...

# How to use multiprocessing.Queue as a FIFO queue:

from multiprocessing import Queue
q = Queue()

q.put('eat')
q.put('sleep')
q.put('code')

>>> q
<multiprocessing.queues.Queue object at 0x1081c12b0>

>>> q.get()
'eat'
>>> q.get()
'sleep'
>>> q.get()
'code'

>>> q.get()
# Blocks / waits forever...
