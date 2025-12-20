from helper import *
from typing import Optional
"""
APPROACH:
- At a given node we check if the tree rooted at this node equal to subtree
    - If yes:- Return True
    - If no:- Search for the subtree in left and right subtree of this node 
"""
# Time: O(m * n)      , m = number of nodes in the main tree (root)    , n = number of nodes in the subtree (subRoot)
# Space: O(h1 + h2)   , h1 = height of the main tree (root)            , h2 = height of the subtree (subRoot)
class Solution:

    # Given two nodes of different tree , I can tell -> "is the tree rooted to these two nodes exactly same"
    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]):  

        """
        - For a tree to be exactly identical, Both tree should have equal:
            - root.val
            - left subtree
            - right subtree
        """
        # Base Case 1:- When both p and q are None nodes
        if not p and not q:
            return True
        
        # Base case 2: one is None, the other is not
        if not p or not q:
            return False
        
        # Base Case 3:- When the p.val and q.val not same
        if p.val != q.val:
            return False

        isLeftSame = self.isSame(p.left, q.left)
        isRightSame = self.isSame(p.right, q.right)

        return isLeftSame and isRightSame

    # Given a main tree root and subtree root, I can tell if subtree lies in main Tree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If main tree is empty, subtree cannot exist
        if not root:
            return False
        
        # Check if trees rooted at this "root" node matches tree rooted at "subRoot" Node 
        if self.isSame(root, subRoot):
            return True
        
         # Otherwise keep searching for the match in left or right subtree
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )



obj = Solution()
root = build_tree([3,4,5,1,2])
subRoot = build_tree([4,1,2])
print(obj.isSubtree(root, subRoot)) 
