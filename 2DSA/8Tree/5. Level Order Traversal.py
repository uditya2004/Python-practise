"""
- Traverse each Node of a tree level wise, moving from left to right

- For this we use BFS algorithm

BFS ALGO
- Initialize an empty list "result", to store final result
- Create a queue and insert the root node.
- While the queue is not empty:
    - Create a list "level" to store current level nodes.

    - (Loop) For each node in the queue:
        - Remove the node from the queue.
        - If it's not None:
            - Add its value to "level".
            - Add its left and right children to the queue.

    - Once done with loop, If level is not empty, add it to result.

- Return the result list.
"""

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# TC: O(N) , visiting each node only once 
# SC: O(N) , for storing nodes in queue
def LevelOrderTraversal(root):
    result = []

    if not root:
        # If the tree is empty,
        # return an empty list
        return result

    q = deque()        # initializing a queue
    q.append(root)     # adding root node to the queue

    while q:           # run until the queue is empty
        level = []
        size = len(q)    # Determine the number of nodes at the current level (size of the queue).

        for i in  range(size):
            node = q.popleft()  # Get the front node in the queue

            level.append(node.data)
                
            # adding the child nodes to the queue, if exists
            if node.left:
                q.append(node.left)  
            
            if node.right:
                q.append(node.right)
        
        if level:  # if level list is not empty then add it to result list
            result.append(level)

    return result


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(LevelOrderTraversal(root))


#      3
#     / \ 
#    9   20
#        / \
#      15   7