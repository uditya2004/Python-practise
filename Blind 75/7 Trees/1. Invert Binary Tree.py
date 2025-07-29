class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        # if the tree is empty return the root node itself
        if not root:
            return root
        
        #swap the children of the root node
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recursively swap the child nodes of the current root's children
        self.invertTree(root.left)    # inverting the left subtree
        self.invertTree(root.right)   # inverting the right subtree

        return root