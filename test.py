"""
Inorder :- Left subtree -> root -> Right Subtree
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def Preorder(root):
    if root != None:
        Preorder(root.left)
        print(root.data)
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