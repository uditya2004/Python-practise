from helper import *
from typing import Optional

"""
- Diameter:- 
    - The diameter is the longest path between any two nodes — these two nodes can be leaf nodes, internal nodes, or even the root.
    - Diameter forming path can or cannot include "root node", both scenario possible

APPROACH:
- CASE:-1 => Diameter forming path includes "root Node"
    - then for the given node diameter is :- left_Height + right_Height

- CASE:- 2 => Diameter forming path NOT including "root Node"
    - then for the given node diameter can be:-
        - left_diameter OR
        - right diameter

        
- SO for a given node diameter will be :- MAX (left_height + right_height + 2,   left_diameter,      right_diameter )

- Here (edge-count definition):
    - height(null) = -1
    - height(leaf) = 0
    - diameter_through_node = left_height + right_height + 2
"""
# Brute Force
#TC: O(N^2) -> For every root node we are calling "height" function
# SC: O(H) -> where H is height of tree
class Solution:

    # TC: O(N)
    # Edge-count definition: height(null) = -1, height(leaf) = 0
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        lh = self.height(root.left)
        rh = self.height(root.right)

        return max(lh, rh) + 1
    
    # TC: O(N)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        diameter_through_root = self.height(root.left) + self.height(root.right) + 2  # diameter_through_root = left_height + right_height + 2
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        # Answer would be the max(diameter_through_root, left_diameter, right_diameter)
        return max(diameter_through_root, left_diameter, right_diameter)



obj = Solution()

root = build_tree([1,2])
print(obj.diameterOfBinaryTree(root)) 

#=========================================================
"""
APPROACH
- We create a global variable "res"
- We traverse through each node of the tree, and for each node we Only find => "diameter_through_root"
- After calculating "diameter_through_root" we update the "res" with max so far

- Finally we return "res"
-------------------------------

Reason:
- Every diameter will pass through a node so if we find all possible diameter_through_node while traversing the entire tree and return the maximum one, that will be our answer(biggest diameter)

"""
# Optimized Solution
# TC: O(N) -> height() visits each node exactly once
# SC: O(H), where H = height of the tree.
class Solution:

    def __init__(self):
        self.res = 0

    # TC: O(N)
    # Edge-count definition: height(null) = -1, height(leaf) = 0
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        lh = self.height(root.left)
        rh = self.height(root.right)

        # EXTRA LINE -> Calculating diameter in height function directly
        # diameter_through_node = lh + rh + 2  (edges on left path + edges on right path + 2 edges connecting subtrees to current node)
        diameter_through_root = lh + rh + 2

        #Updating "res"
        self.res = max(self.res, diameter_through_root)

        return max(lh, rh) + 1

    # TC: O(N)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.height(root)   # TC: O(N)

        return self.res



obj = Solution()

root = build_tree([1,2])
print(obj.diameterOfBinaryTree(root)) 
