from helper import *
from typing import Optional

# Brute Force
# TC: O(N * N) => it visited each node so O(N), and for each not we find height , so O(N*N)
"""
- Diameter:- 
    - Length of the longest path between any two nodes (Note:- both of those nodes should always be leaf node )
    - Diameter forming path can or cannot include "root node", both scenario possible

APPROACH:
- CASE:-1 => Diameter forming path includes "root Node"
    - then for the given node diameter is :- left_Height + right_Height

- CASE:- 2 => Diameter forming path NOT including "root Node"
    - then for the give node diameter can be:-
        - left_diameter OR
        - right diameter

        
- SO for a given node diameter will be :- MAX (left_height + right_height,   left_diameter,      right_diameter )
"""
# class Solution:

#     # TC: O(N)
#     def height(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         lh = self.height(root.left)
#         rh = self.height(root.right)

#         return max(lh, rh) + 1

#     # TC: O(N)
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

#         if not root:
#             return 0
        
#         #CASE 1
#         left_height = self.height(root.left)
#         right_height = self.height(root.right)

#         diameter_through_root = left_height + right_height

#         # CASE 2
#         left_diameter = self.diameterOfBinaryTree(root.left)
#         right_diameter = self.diameterOfBinaryTree(root.right)

#         return max(diameter_through_root, left_diameter, right_diameter)



# obj = Solution()

# root = build_tree([1,2])
# print(obj.diameterOfBinaryTree(root)) 

#=========================================================
"""
APPROACH
- We create a global variable "res"
- We traverse through each node of the tree, and for each node we Only find => "diameter_through_root"
- After calculating "diameter_through_root" we update the "res" with max so far

- Finally we return "res"
-------------------------------

Reason:
- As we traverse through the entire tree, while updating "res" => we will eventually find left_diameter and right_diameter along the recursion
- So no need to find left and right diameter for each node


"""
class Solution:

    def __init__(self):
        self.res = 0

    # TC: O(N)
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        lh = self.height(root.left)
        rh = self.height(root.right)

        # EXTRA LINE -> Calculating diameter in height function directly
        # Even though height counts nodes, lh + rh naturally becomes an edge count.
        diameter_through_root = lh + rh

        #Updating "res"
        self.res = max(self.res, diameter_through_root)

        return max(lh, rh) + 1

    # TC: O(N)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.height(root)

        return self.res



obj = Solution()

root = build_tree([1,2])
print(obj.diameterOfBinaryTree(root)) 
