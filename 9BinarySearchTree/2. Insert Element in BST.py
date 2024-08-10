"""
- In Insertion:-
        - If the Node is already present in the tree, do not make any changes
        - If not present, newly inserted node will always be a leaf node
        - Follow BST Properties while inserting an element.
                - node.data < root.data, then it will be inserted in the left 
                - node.data > root.data, then it will be inserted in the right. 
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

#Method 1 - Insertion in BST using Recursion:
#TC: O(H) , it's same as search
#SC: O(H)
def Insert(root,key):
    if root == None:      # If the tree is empty, we return the New node , which finally become root node a function call line.
        return Node(key)
    
    elif root.data == key:  #If key already present in the tree, do not make any changes, we return the same root.
        return root
    
    elif root.data > key:
        root.left  = Insert(root.left,key)

    else:
        root.right = Insert(root.right,key)
    
    return root


#Method 2 - Insertion in BST using Iterative:
#TC: O(H) , it's same as search
#SC: O(1)
def Insert2(root,key):
    parent = None    # For keeping track of "curr" 's root
    curr = root

    while curr != None:         # This loop will take us to the node below which element is to be inserted and that node will be stored in "parent"
        parent = curr

        if curr.data == key:    # If key already present in the tree, do not make any changes, we return the same root.
            return root
        
        elif curr.data < key:   # If key is greater than current node's data, move to the left subtree
            curr = curr.left
        
        else:                   # If key is smaller than current node's data, move to the right subtree
            curr = curr.right
    
    if parent == None:          # For Empty Tree, create a new node and return it as the root
        return Node(key)
    
    # Inserting the new node to the left or right of the node
    if parent.data > key:     
        parent.left = Node(key)     
    
    else:
        parent.right = Node(key)
        
    return root                 # Finally returning the root of the Tree with the new node.


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.right.left = Node(12)
root.right.right = Node(18)

root = Insert(root,20)





#---------------------------------------------------
#Printing Tree(not in syllabus)
def getHeight(root):
    return 1 + max(getHeight(root.left), getHeight(root.right)) if root else 0

def printTree(root):
    def fillMatrix(matrix, node, row, col, width):
        if node:
            mid = width // 2
            matrix[row][col + mid] = str(node.data)
            if node.left:
                matrix[row + 1][col + mid - 1] = '/'
                fillMatrix(matrix, node.left, row + 2, col, mid)
            if node.right:
                matrix[row + 1][col + mid + 1] = '\\'
                fillMatrix(matrix, node.right, row + 2, col + mid + 1, mid)

    height, width = getHeight(root) * 2, 2 ** getHeight(root) - 1
    matrix = [[' ' for _ in range(width)] for _ in range(height)]
    fillMatrix(matrix, root, 0, 0, width)
    print('\n'.join(''.join(row).rstrip() for row in matrix if any(cell != ' ' for cell in row)))

print("Visual representation of the tree:")
printTree(root)
