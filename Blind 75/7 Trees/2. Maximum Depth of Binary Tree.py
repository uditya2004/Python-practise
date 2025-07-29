import math
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root) -> int:
        result = -math.inf

        if not root:
            return 0
        node = root.left
        count = 1
        while node != None:
            pass