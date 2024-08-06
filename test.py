import math
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
    10
    / \ 
 20    30
       / \
     40   50
"""

def Getmax(root):
    if root == None:
        return -math.inf
    else:
        left_subtree_max = Getmax(root.left)
        right_subtree_max = Getmax(root.right)

        return max(left_subtree_max, right_subtree_max, root.data)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

Getmax(root)