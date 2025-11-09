class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        i = 0
        minLength = float('inf')

        currSum = 0
        for j in range(0,len(nums)):

            currSum += nums[j]
            
            # Until the currsum >= target we keep on shrinking the window and update the minLength along the way.
            while currSum >= target:
                minLength = min(minLength, j-i+1)
                currSum -=nums[i]
                i+=1
        
        if minLength == float('inf'):  # no such subarray found
            return 0 
        else:
            return minLength
        
obj = Solution()
target = 11
nums = [1,1,1,1,1,1,1,1]
print(obj.minSubArrayLen(target, nums))