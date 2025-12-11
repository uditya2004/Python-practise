"""
SLOW FAST POINTER Use-case:-

1. Cycle Detection in Linked List
    - Eg:- Detecting Duplicate Number in Array
2. Finding the Middle of a Linked List
"""

class Solution:
    def findDuplicate(self, nums) -> int:
        """
        APPROACH:- SLOW FAST POINTER (USED FOR CYCLE DETECTION)
        We create a Linked List and it will have cyle:-
            - List indexes act as -> Node value 
            - List values act as -> Next pointer

        1. Take a slow and fast pointer:-
            - slow move 1 step at a time
            - fast moves 2 steps at a time
        Stop when the slow == fast.

        2. Now place another slow pointer at the beginning of the formed Linked List
            - Move the 2nd and the 1st slow pointer 1 step at a time simultaneously , until both the slow pointers meet.
            - the node at which they meet is the required answer.   (FACT that the distance between new_slow and old_slow from the element at the start of cycle will be always same => can be proved mathematically)
        """
        # moving the fast and slow pointers until they meet
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]         # moving slow 1 step in the imagined linked List
            fast = nums[nums[fast]]   # moving fast 2 steps in the imagined Linked List
            if slow == fast:
                break

        # moving slow and another slow pointer until they meet. Return the node where they meet.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow2


nums = [1,3,4,2,2]
obj = Solution()
print(obj.findDuplicate(nums))