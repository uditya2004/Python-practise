"""
Postorder :- Left subtree -> Right Subtree -> Root

Post= Root last
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#TC: O(N) , We visit every node exactly Once
#SC: O(H) , H is max no. of entries in function call stack. In one pass, atmost head to leaf nodes will be present in the function call stack.

def Postorder(root):
    if root!= None:
        Postorder(root.left)
        Postorder(root.right)
        print(root.data, end = " ")

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
Postorder(root)


"""
Note: 
→ In inorder and preorder , last thing that happens is recursive call, whereas in postorder last thing that happens is printing operation.
→ So for compilers that do tail call optimization, inorder and preorder are better than postorder. 
→ So if you have a choice between inorder, preorder, postorder - You should either choose inorder and preorder.
"""