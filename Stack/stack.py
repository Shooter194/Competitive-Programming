
from queue import LifoQueue


stack = LifoQueue(maxsize = 3)

stack.put(1)
stack.put(2)
stack.put(3)

print (stack.qsize(),stack.full())

print (stack.get())
print (stack.get())
print (stack.qsize(),stack.full())
print (stack.get())


################################ Using dequeue module

from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print (len(stack))

print (stack.pop())
print (stack.pop())
print (stack.pop())

print (len(stack))
