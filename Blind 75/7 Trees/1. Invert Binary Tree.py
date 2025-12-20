from helper import *
from typing import Optional

# TC: O(N), where n is number of nodes => As we visited each node only once
# SC: O(H), where H is height of tree => Due to recursion stack 
class Solution:

    """
    - We visit each node one by one using preorder traversal.
        - For each node, we swap the left and right subtree.
        - Recursively call for the left and right children
    
    - Edge Case:- if root root is None , return None
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if the tree is empty return the root node itself
        if not root:    # root is None (tree empty)
            return root
        
        # swap the left and right subtree
        # eg:- root.left is the root of left subtree, swaping it with right means swapping entire left subtree (not just single node)
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recursively swap the child nodes of the current root's children
        self.invertTree(root.left)    # inverting the left subtree
        self.invertTree(root.right)   # inverting the right subtree

        return root


obj = Solution()

root = build_tree([4,2,7,1,3,6,9])
result = obj.invertTree(root)

print(tree_to_list(result))  
