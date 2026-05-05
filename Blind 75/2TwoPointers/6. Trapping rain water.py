# Method:- Better approach - > Prefix array approach -> Three separate loops
#TC: O(3N)
# SC: O(2N)
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


#==============================
#Method:- Best Approach -> Two pointer approach -> Single loop
# TC: O(N)
# SC: O(1)
class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0 

        l= 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]

        result = 0

        while l < r:
            """
            - Shift the smaller pointer (i.e l forward or r backward)
            """
            if leftMax < rightMax:
                l +=1                              # Move left pointer forward
                leftMax = max(leftMax, height[l])  # Update leftMax
                result +=leftMax - height[l]       # Update result

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        
        return result

    
obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(obj.trap(height))