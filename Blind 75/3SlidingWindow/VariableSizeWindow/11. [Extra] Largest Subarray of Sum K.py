# Return maximum length of a subarray whose sum <= K
# Assumption: arr contains non-negative numbers
class Solution:
    def longestSubarray(self, nums, k) -> int:  
        result = 0 # max size of subarray

        currSum = 0
        n = len(nums)

        i = 0
        j = 0
        while j < n:
            # 1. CALCULATION
            # Add incoming element
            currSum += nums[j]

            # 2. SHRINK
            # Invalid condition: currSum > K
            while currSum > k:
                currSum -= nums[i]
                i +=1

            # 3. RECORD
            # Now currSum <= K, so window is valid
            if currSum == k:
                result = max(result, j-i+1)

            # 4. MOVE j
            j += 1

        return result


obj = Solution()
nums = [4,1,1,1,2,3,5]
k = 5
print(obj.longestSubarray(nums, k))