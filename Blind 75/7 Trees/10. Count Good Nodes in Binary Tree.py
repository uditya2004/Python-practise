from typing import Optional
from helper import *

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            
            # if the node if good, set res = 1 else 0
            res = 1 if node.val >= maxVal else 0

            maxVal = max(maxVal, node.val)

            # counting the number of good nodes from left and right subtree and add it to "res"
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        # Doing DFS for entire tree
        return dfs(node = root, maxVal = root.val)

    
        


        
    

obj = Solution()
root = build_tree([3,3,None,4,2])
print(obj.goodNodes(root))