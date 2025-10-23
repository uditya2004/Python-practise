
# TC: O(N)
# SC: O(1)
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]

            if sum < target:
                left +=1
            elif sum > target:
                right -=1
            else:
                return [ left + 1, right + 1]


numbers = [-1,0]
target = -1
obj = Solution()
print(obj.twoSum(numbers, target))