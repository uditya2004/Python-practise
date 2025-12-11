from typing import Optional
from helper import build_list, ListNode, print_list

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # finding the mid point using the fast and slow pointer.
        """
        when the fast pointer reaches the end , slow pointer will reach the mid point.
        """
        fast = head
        slow = head
        while fast != None and fast.next != None:
             slow = slow.next
             fast = fast.next.next
        

        # reverse the 2nd half
        prev = None
        second = slow.next   # second half start from the next element of mid element

        slow.next = None  # after copying the value of slow.next , assigning it to None breaks the 1st and 2nd half properly

        while second != None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        

        # merging 1st and 2nd half
        curr1 = head      # pointer pointing to the 1st half head
        curr2 = prev      # pointer pointing to the 2nd half head
        while curr2 != None:
            # storing the next node address of both pointers
            temp1 = curr1.next
            temp2 = curr2.next

            # Making links as aspected in question
            curr1.next = curr2
            curr2.next = temp1

            # Move both pointer inwards (to there next nodes)
            curr1 = temp1
            curr2 = temp2
        

obj = Solution()

head = build_list([1,2,3,4])

obj.reorderList(head)

print("Answer List:")
print_list(head)