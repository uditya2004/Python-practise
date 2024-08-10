"""
Inorder :- Left subtree -> root -> Right Subtree
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#TC: O(N)
#SC: O(H)
def Search(root, data):
    if root == None:
        return False
    
    if root.data == data:
        return True
    elif root.data < data:
        return Search(root.right,data)
    else:
        return Search(root.left,data)

def Search2(root,data):
    while root != None:
        if root.data == data :
            return True
        
        elif root.data> data:
            root = root.left
        
        else:
            root = root.right

    return False
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
print(Search2(root,0))