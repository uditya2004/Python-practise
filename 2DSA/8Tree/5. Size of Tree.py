
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


#As as we are going through every node, TC and SC will be same as Traversal i.e  TC: O(N) , SC:O(H)
#Method - 1
def Treesize(root):
    if root == None:
        return 0
    
    #For Traversal we can use any type(inorder or postorder or Preorder)
    # this function uses post-order traversal.
    else:
        Left_Subtree_size = Treesize(root.left)             # Recursively find the size of the left subtree and store it in "LeftSubtree_size"
        Right_Subtree_size = Treesize(root.right)           # Recursively find the size of the right subtree and store it in "RightSubtree_size"

        return Left_Subtree_size + Right_Subtree_size + 1    # Adding extra "1" for counting root node


#Method 2 - Shorted Implementation
def Treesize2(root):    
    if root == None:
        return 0
    
    else:
        return Treesize(root.left) + Treesize(root.right) + 1    
    

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

#-----------
#Finding Size

print(Treesize(root))



"""
    10
    / \ 
 20    30
       / \
     40   50
"""




