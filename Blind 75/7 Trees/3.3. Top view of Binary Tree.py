from helper import *
from typing import Optional
from collections import deque

"""
CONCEPT: Top View of a Binary Tree

The "top view" is what you see when you look at the tree from directly above.

CONCEPT — Horizontal Distance (HD):
  - Assign every node a horizontal distance relative to the root.
    - Root         → HD = 0
    - Left child   → parent's HD => - 1
    - Right child  → parent's HD => + 1

Example tree built from [3, 9, 20, 15, 7]:

          3         HD:  0
         / \\
        9  20       HD: -1, +1
          /  \\
         15   7     HD:  0, +2

  Vertical columns:
    HD -1 → [9]
    HD  0 → [3, 15]   ← only 3 is visible from top
    HD +1 → [20]
    HD +2 → [7]

  Top view result (sorted by HD): [9, 3, 20, 7]

ALGORITHM — BFS with HD tracking:

"""
class Solution:
    def topView(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []    # empty tree, nothing to show from top

        # Dictionary storing pair => horizontal_distance : node.val
        hd_map = {}

        # Queue storing a pair value => (node, horizontal_distance)
        q = deque()
        q.append((root, 0))

        while q:
            node, hd = q.popleft()

            # Only record the first node at each horizontal distance
            if hd not in hd_map:
                hd_map[hd] = node.val

            if node.left:
                q.append((node.left, hd - 1))

            if node.right:
                q.append((node.right, hd + 1))

        # Return values sorted by horizontal distance (left to right)
        return [hd_map[hd] for hd in sorted(hd_map)]  # sorted the dict as per Horizontal distance



obj = Solution()
root = build_tree([3,9,20,15,7])
result = obj.topView(root)

print(result)
