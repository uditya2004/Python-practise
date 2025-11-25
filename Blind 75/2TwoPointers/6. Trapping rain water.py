"""
- for any i
    - water[i] = min(max_height_in_left , max_height_in_right) - arr[i]

- result = summation of all water[i]
- (where arr[i] is the height of the building) 
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)

        # building max height in left array of current element (include:- currently standing element + left array)
        maxLeft = [0]*n 

        for i in range(0,len(height)):
            
            if i == 0:
                maxLeft[i] = height[i]
            else:
                maxLeft[i] = max(height[i], maxLeft[i-1])
        
        # building max height in right array of current element (include:- currently standing element + left array)
        maxRight = [0]*n
        
        for i in range(n - 1, -1, -1):
            if i == n-1:
                maxRight[i] = height[i]
            else:
                maxRight[i] = max(height[i], maxRight[i+1])
        
        # finding result directly without using water[i] but concept remains same
        result = 0
        for i in range(0, len(height)):
            result += min(maxLeft[i], maxRight[i]) - height[i]
        
        return result

obj = Solution()
height = [4,2,0,3,2,5]
print(obj.trap(height))