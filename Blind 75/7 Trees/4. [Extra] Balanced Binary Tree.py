from helper import *
from typing import Optional

# TC:- O(N), Each node is visited once.
# SC:- O(H), Where H is the height of the tree (due to the recursion stack).
class Solution:
    def __init__(self) -> None:
        self.res = True

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)

        if (abs(lh-rh)) > 1:
            self.res = False

        return max(lh, rh) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.height(root)

        return self.res 



obj = Solution()

root = build_tree([])
print(obj.isBalanced(root)) 


#=======================================
#=======================================
# Minor optimization => Early exit

# TC:- O(N), Each node is visited once.
# SC:- O(H), Where H is the height of the tree (due to the recursion stack).
# class Solution:
    
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
#         """
#         - Problem in previous solution:- 
#             - Even after the tree is found unbalanced, recursion continues unnecessarily.

            
#         Optimization:-
#         - -1 cleanly represents “unbalanced”
#             - Allows early termination
#         """
#         def height(root: Optional[TreeNode]) -> int:
#             if not root:
#                 return 0
#             lh = height(root.left)
#             if lh == -1:            # Means:- Height information is no longer valid, function should immediately move upward
#                 return -1
            
#             rh = height(root.right)
#             if rh == -1:
#                 return -1
        
#             if (abs(lh-rh)) > 1:
#                 return -1

#             return max(lh, rh) + 1
        
#         return height(root) != -1



# obj = Solution()

# root = build_tree([])
# print(obj.isBalanced(root)) 
