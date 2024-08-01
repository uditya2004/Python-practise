"""
(Follows FIFO - First in First Out)
"""

#Queue Implementation using List
lst = []

#Enqueue Operation - Adding Elements in a queue  (Add at the end of list)
lst.append(10)
lst.append(20)
lst.append(30)

#Dequeue Operation - Removing elements from a queue   (Remove elements from the start of the list)
print(lst.pop(0))


#Rear Element (last element in the list)
print(lst[-1])

#Front element (1st element in the list)
print(lst[0])

#Length of the queue
print(len(lst))

"""
Disadvantage of using List Implementation:
- "append()" operation is amortized O(1) , but "pop(0)" operation is O(N)
"""


#================================
#Implementation of Queue using DEQUE
from collections import deque

q = deque()

#Enqueue Operations
q.append(10)
q.append(20)
q.append(30)

#Dequeue Operations
print(q.popleft())

#Length of the queue
print(len(q))

#Front Element
print(q[0])

#Rear element
print(q[-1])

"""
- It is better than list implementations as:
    -- Both "pop(0)" and "append()" operations are O(1)
"""