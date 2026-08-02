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
        """
        - Base cases are handled properly:
            - If both root and subRoot are None → True (empty tree is subtree of empty tree)
            - If root exists but subRoot is None → True (empty tree is subtree of any tree)
            - If root is None but subRoot exists → False (can't find a non-empty subtree in an empty tree)
        """
        if (not root and not subRoot) or (root and not subRoot):
                    return True
        
        if not root and subRoot:
            return False
        
        if self.isSame(root, subRoot):
            return True

        # now same above process we have to repeat for left and right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



obj = Solution()
root = build_tree([3,4,5,1,2])
subRoot = build_tree([4,1,2])
print(obj.isSubtree(root, subRoot)) 


# ======================================
# Just a Shorter way of writing this
class Solution:

    # Given two nodes of different tree , I can tell -> "is the tree rooted to these two nodes exactly same"
    def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        return (p.val == q.val) and self.isSame(p.left, q.left) and self.isSame(p.right, q.right)

    # Given a main tree root and subtree root, I can tell if subtree lies in main Tree
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


obj = Solution()
root = build_tree([3,4,5,1,2])
subRoot = build_tree([4,1,2])
print(obj.isSubtree(root, subRoot)) 