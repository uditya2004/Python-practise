"""
APPROACH
- For each building in "heights" array => we find how much we can expand it to left and right, keeping height as same.
    - For this we do like this:
        - Keep moving to right till you find a building whose height smaller than current
        - Keep moving to left till you find a building whose height smaller than current.
    - This way :
        - "height" we get from => current building height
        - "width" we get from => how far we are able to stretch left and right
    - Now, area = height * width

- Finally return maximum area seen so far.
"""

# Combination of Nearest smaller to right and left pattern

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        
        # Nearest smaller to right -> give how far we can stretch to the right
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
        # Nearest smaller to left -> give how far we can stretch to the left
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