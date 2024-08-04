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

def SearchData(root, data):
    if root == None:
        return False
    
    if root.data == data:
        return True 
    
    return SearchData(root.left, data) or SearchData(root.right, data)        


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)


print(SearchData(root, 50))