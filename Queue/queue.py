
######  Implement queue with queue module

from queue import Queue

q = Queue( maxsize = 3 )

q.put(1)
q.put(2)
q.put(3)
q.put(4)

print (q.size())

print (q.get())
print (q.get())
print (q.get())

print (q.size())

###### Implement Queue with deque module ####


from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print (len(queue))

print (queue.popleft())
print (queue.popleft())
print (queue.popleft())

print (len(queue))

