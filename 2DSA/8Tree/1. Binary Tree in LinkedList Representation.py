"""
→ In binary tree every node has atmost 2 children. In other words , degree of any node is = atmost 2
→ Degree of a Node: No. of children of a Node

→ For eg:
    30
    / \ 
 40    50
 /     / \
70   60   80

Note: 
→ Every Node will have 1 data and 2 reference field (left and right). 
→ Both reference fields, are initially set to None. 
→ Leaf Node, will have both reference set to None, as they don't have any children.

"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(20)
root.right = Node(30)

root.left.left = Node(40)


"""
    10
    / \ 
 20    30
 /     
40   
"""

# #================
#Empty Binary Tree Representation

root = None

#To check if the Tree is empty or not, check if the root is None or not.
