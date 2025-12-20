from typing import Optional
from helper import *

class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            
            #empty tree is still a BST
            if not node:
                return True
            
            # if not satisfying conditon of BST then return False
            if not (left < node.val < right):
                return False
            
            """
            - do recursive call for left:-
                - keep the left boundary same, 
                - update the right boundary to => current root (nod.val)

            - Do recursive call for right:-
                - keep the right boundary same
                - update the left boundary to => current root (node.val)
            """
            return (
                valid(node.left, left, node.val) and valid(node.right, node.val, right)
                )
        
        # Calling for Tree's Root, keeping left and right boundary -inf and inf, as -inf<root<inf
        return valid(root, float('-inf'), float('inf'))


obj = Solution()
root = build_bst([5,1,4,None,None,3,6])
print(obj.isValidBST(root))