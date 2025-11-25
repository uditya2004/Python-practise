"""
APPROACH
- From the currently standing building we find smaller building than this on both the side , this will give the maxium width of our rectangle possible w.r.t current building
- So we do following:-
    - Build right[] :- Nearest smaller to the right array
    - Build left[] :- Nearest smaller to the left array
    - width[]:- right[i] - left[i] - 1
    - area[]:- width[i] * heights
    - Then find the max(area)
"""

# Combination of Nearest smaller to right and left pattern

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        
        # Nearest smaller to right
        rightMost = []   # store index
        stack = []
        for i in range (n-1, -1, -1):

            if not stack: # stack empty
                rightMost.append(n)
            else: # not empty

                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                
                if not stack:      # popping made it empty, no element smaller
                    rightMost.append(n)
                else:
                    rightMost.append(stack[-1])
                
            stack.append(i)
        rightMost = list(reversed(rightMost))

        # ====================================================
        # Nearest smaller to left
        leftMost = []   # store index
        stack = []
        for i in range (0, n):

            if not stack: # stack empty
                leftMost.append(-1)
            else: # not empty

                while stack and heights[i] <= heights[stack[-1]]:
                    stack.pop()
                
                if not stack:      # popping made it empty, no element smaller
                    leftMost.append(-1)
                else:
                    leftMost.append(stack[-1])
                
            stack.append(i)

        #=====================================================
        area = []

        for i in range(0, n):
            width = rightMost[i] - leftMost[i] - 1
            area.append(width * heights[i])

        return max(area)
        




obj = Solution()
heights = [2,4]
print(obj.largestRectangleArea(heights))