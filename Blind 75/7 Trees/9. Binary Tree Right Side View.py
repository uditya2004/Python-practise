from typing import Optional
from helper import *
from collections import deque

class Solution:

    """
    - Do a level order traversal, but instead of appending complete level list to result, just append level[-1] (i.e the rightmost element on the level)
    """
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []

        if not root:
            return result
        
        q = deque()
        q.append(root)

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            
            if level:
                result.append(level[-1])
        
        return result


    

obj = Solution()
root = build_tree([])
print(obj.rightSideView(root))