"""
Find the node in the tree having the maximum value
"""

import math

class Node:
    def __init__(self,data):
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
#TC: O(N) , SC: O(H)  - same as traversal

#Method -1 
def Getmax(root):
    if root == None:
        return -math.inf    #Returning -infinity when root is none
    
    else:
        left_subtree_max = Getmax(root.left)          # Recursively find the max element in the left subtree
        right_subtree_max = Getmax(root.right)        # Recursively find the max element in the right subtree

        return max(left_subtree_max, right_subtree_max, root.data)
    
#Method - 2 : Shorter Implementation
def Getmax2(root):
    if root == None:
        return -math.inf    #Returning -infinity when root is none
    
    else:
        return max(Getmax(root.left), Getmax(root.right), root.data)

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

#-----------
#Finding Size

print(Getmax(root))



