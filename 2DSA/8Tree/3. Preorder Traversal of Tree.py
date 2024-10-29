"""
Preorder :- Root -> Left subtree -> Right Subtree
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#TC: O(N) , We visit every node exactly Once
#SC: O(H) , H is max no. of entries in function call stack. In one pass, atmost head to leaf nodes will be present in the function call stack.

def Preorder(root):
    if root!= None:
        print(root.data, end = " ")
        Preorder(root.left)
        Preorder(root.right)

#Creating a Binary Tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.right.left = Node(40)
root.right.right = Node(50)
"""
    10
    / \ 
 20    30
       / \
     40   50
"""

#============
Preorder(root)