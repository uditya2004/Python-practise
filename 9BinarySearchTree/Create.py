"""
- In BST, Every Node on the left is smaller and nodes on the right are bigger than the root node.
- All Nodes are distinct
- Linked Data Structure
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
"""
    18
    / \
   16  30
       / \
      20  100    
""" 

def BinarySearch(root,data):
    if root == None:
        return False
    elif root.data == data:
        return True
    
    if data> root.data:
        return BinarySearch(root.right, data)
    else:
        return BinarySearch(root.left, data)

root = Node(18)
root.left = Node(16)
root.right = Node(30)
root.right.left = Node(20)
root.right.right = Node(100)

print(BinarySearch(root, 1))