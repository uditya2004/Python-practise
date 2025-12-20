from helper import *
from typing import Optional
"""
- In a BST:
    - Left subtree values < root value
    - Right subtree values > root value

- In a regular binary tree, we'd have to do a full DFS/BFS and check both left and right subtrees every time. That's O(n).
- But in a BST, we can use the ordering property! We can decide which direction to go based on comparing values. This makes it more like O(h) where h is height.
"""
# Time: O(h)
# Space: O(h)
class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:  # means:- This subtree does not contain an LCA
            return None
        
        # If p.val < root.val and q.val < root.val → LCA is in left
        if p.val < root.val and q.val < root.val:       
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If p.val > root.val and q.val > root.val → LCA is in right
        if p.val > root.val and q.val > root.val:        
            return self.lowestCommonAncestor(root.right, p, q)

        # Otherwise, if both p and q is not on same, side then the root from where there is a split path for p and q that is LCA → this node is the LCA
        return root

obj = Solution()
root = build_bst([2,1])
p=TreeNode(2)
q=TreeNode(1)
print(obj.lowestCommonAncestor(root, p, q)) 
