from helper import *
from typing import Optional

# TC: O(N), where n is number of nodes => As we visited each node only once
# SC: O(H), where H is height of tree => Due to recursion stack 
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        lh = self.maxDepth(root.left)
        rh = self.maxDepth(root.right)

        return max(lh, rh) + 1    


obj = Solution()

root = build_tree([1, None, 2])
print(obj.maxDepth(root)) 
