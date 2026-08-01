from helper import *
from typing import Optional

# Brute force
# TC: O(N^2) => same node is visited over and over again

class Solution:
    # TC: O(N) => every node in this subtree is visited exactly once
    # SC: O(H) => recursion stack goes as deep as the height H
    #             (H = N for a skewed tree, log N for a balanced tree)
    def height(self, root) -> int:
        if not root:
            return -1 # None node return -1

        return max(self.height(root.left), self.height(root.right)) + 1

    # TC: O(N^2) => for each of the N nodes we call height() which itself is O(N).
    #               Height of the same subtree is recomputed again and again
    #               (O(N * H): N^2 for a skewed tree, N log N for a balanced tree)
    # SC: O(H) => only the recursion stack (isBalanced + height nest up to height H)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # As per question: if Null tree return True
        if not root:
            return True

        # We find the height of the left and right subtree
        lh = self.height(root.left)
        rh = self.height(root.right)

        """
        - if the difference of lh and rh is > 1, then not balance
        - Else we check for left and right subtree (same process repeats)
        """
        if abs(lh - rh) > 1:
            return False

        if self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

obj = Solution()
root = build_tree([])
result = obj.isBalanced(root)

print(result)

#======================================
# Better solution
# TC: O(N) => every node is visited exactly once (height is computed bottom-up, no recomputation)
# SC: O(H) => recursion stack only

class Solution:
    # TC: O(1) => just initialising a flag
    # SC: O(1) => one boolean stored
    def __init__(self):
        self.res = True

    # TC: O(N) => single post-order pass, each node processed once,
    #             children's heights are reused instead of recalculated
    # SC: O(H) => recursion stack depth = height of tree
    def height(self, root) -> int:
        if not root:
            return -1 # None node return -1

        lh = self.height(root.left)
        rh = self.height(root.right)

        if abs(lh - rh) > 1:
            self.res = False
        
        return max(lh, rh) + 1

    # TC: O(N) => one call to height() which traverses all N nodes once
    # SC: O(H) => recursion stack of height(); H = N (skewed) / log N (balanced)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.height(root)

        return self.res



obj = Solution()
root = build_tree([])
result = obj.isBalanced(root)

print(result)



#=======================================
#=======================================
# Minor optimization => Early exit

# TC:- O(N), Each node is visited once.
# SC:- O(H), Where H is the height of the tree (due to the recursion stack).
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        """
        - Problem in previous solution:- 
            - Even after the tree is found unbalanced, recursion continues unnecessarily.

            
        Optimization:-
        - -1 cleanly represents “unbalanced”
            - Allows early termination
        """
        def height(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            lh = height(root.left)
            if lh == -1:            # Means:- Height information is no longer valid, function should immediately move upward
                return -1
            
            rh = height(root.right)
            if rh == -1:
                return -1
        
            if (abs(lh-rh)) > 1:
                return -1

            return max(lh, rh) + 1
        
        return height(root) != -1



obj = Solution()

root = build_tree([])
print(obj.isBalanced(root)) 
