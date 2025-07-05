"""
Inorder :- Left subtree -> Root -> Right Subtree

- Recursively goes left as far as possible
- Move up till the root
- Then moves right till bottom
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

#TC: O(N) , We visit every node exactly Once
#SC: O(H) , H is max no. of entries in function call stack.

def Inorder(root):
    if root != None:
        Inorder(root.left)              # Recursively Traversing the left subtree
        print(root.data, end= " ")      # Printing the root Node
        Inorder(root.right)             # Recursively Traversing the Right subtree
 
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
#Finding the inorder Traversal
Inorder(root)
