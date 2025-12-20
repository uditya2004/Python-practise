from helper import *
from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        """
        - For a tree to be exactly identical:-
            - root.val of both tree same
            - left subtree of both tree same
            - right subtree of both tree same
        
        - All 3 condition should be TRUE to say both tree are same
        """
        # Base Case 1:- When both p and q are None nodes
        if not p and not q:
            return True
        
        # Base case 2: one is None, the other is not
        if not p or not q:
            return False

        return (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



obj = Solution()
p = build_tree([1,2,3])
q = build_tree([1,2,3])
print(obj.isSameTree(p, q)) 
