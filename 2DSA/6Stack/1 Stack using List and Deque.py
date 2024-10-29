#IMPLEMENT STACK USING LIST

# lst = []

# #Push Elements in a Stack
# lst.append(10)
# lst.append(20)
# lst.append(30)

# #Pop Element from a stack
# print(lst.pop())

# #Peek Operations in a stack
# top = lst[-1]
# print(top)

# #Size() Operation in stack
# size = len(lst)
# print(size)

# #isEmpty Operation in Stack
# if lst == []:
#     print("Empty")
# else:
#     print("Not Empty")

#======================================
#IMPLEMENT STACK USING DEQUE   (Deque is mainly based on doubly linked list data structure)
from collections import deque   

stack = deque()

#Push Elements in a Stack
stack.append(10)
stack.append(20)
stack.append(30)

#Pop Element from a stack
print(stack.pop())

#Peek Operations in a stack
top = stack[-1]
print(top)

#Size() Operation in stack
size = len(stack)
print(size)


#===============

"""
- In List, push and pop operation has TC: Amortized - O(1)
- List
    advantages:-
        - It's cache friendly, as it's an array implementation and elements are at contiguous memory location
    Disadvantage:-
        - Worst ccase TC is O(N) , as it is amortized O(1) - which means on average it's O(1) but there might be a worst case which can take more time

====================================
- In Deque, push and pop operation has TC: Worst case - O(1)
    advantage:-
        - TC: Worst case O(1), as we use doubly linked list implementation
    disadvantage
        - It's not cache friendly, as it is doubly linked list implementation, elements are stored anywhere in the memory
"""