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
                - If we shifted l forward:
                    - 
            """
            if leftMax < rightMax:
                l +=1
                leftMax = max(leftMax, height[l])
                result +=leftMax - height[l]

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        
        return result

    
obj = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(obj.trap(height))