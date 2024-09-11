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
#TC: O(N), SC: O(H)
#Method - 1
def SearchData(root, data):
    if root == None:
        return False
    
    elif root.data == data:
        return True 
    
    elif SearchData(root.left, data) == True:
        return True
    
    else:
        return SearchData(root.right, data) 

#Method 2
def SearchData2(root, data):
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