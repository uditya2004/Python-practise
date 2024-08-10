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
#Printing Tree (Not in Syllabus)

def print_tree(root):
    if not root:
        return
    
    # Level order traversal using a queue
    queue = [(root, 0)]
    levels = {}
    
    while queue:
        node, level = queue.pop(0)
        if level not in levels:
            levels[level] = []
        levels[level].append(node)
        
        if node:
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
    
    max_level = max(levels.keys())
    for level in range(max_level + 1):
        if level > 0:
            # Printing connectors
            connectors = []
            for node in levels[level - 1]:
                if node:
                    if node.left:
                        connectors.append("/")
                    else:
                        connectors.append(" ")
                    if node.right:
                        connectors.append("\\")
                    else:
                        connectors.append(" ")
                else:
                    connectors.append("  ")
            print(" " * (max_level - level) + " ".join(connectors))
        
        # Printing node values
        values = []
        for node in levels[level]:
            if node:
                values.append(str(node.data))
            else:
                values.append(" ")
        print(" " * (max_level - level) + " ".join(values))
print_tree(root)