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
"""
    18
    / \
   16  30
       / \
      20  100    
""" 
#METHOD 1: RECURSIVE METHOD
# TC: O(H), in the worst case we will traverse across the height
# Auxilary Space: O(H), we store all the node across the height and extra None at the end, in worst case
def BinarySearch(root,data):
    if root == None:
        return False
    elif root.data == data:
        return True
    
    if data> root.data:                            # If data is bigger than root, we only search in the right subtree , ignoring complete leftsubtree and vice versa
        return BinarySearch(root.right, data)
    else:
        return BinarySearch(root.left, data)
#----------------------------------------

#METHOD - 2: ITERATIVE METHOD  (Better)
# TC: O(H), in the worst case we will traverse across the height
#SC: O(1)
def BinarySearch2(root,key):
    while root != None:
        if root.data == key:
            return True
        
        elif root.data < key:
            root = root.left
        else:
            root = root.right

    return False

root = Node(18)
root.left = Node(16)
root.right = Node(30)
root.right.left = Node(20)
root.right.right = Node(100)

print(BinarySearch2(root, 1))

print_tree(root)