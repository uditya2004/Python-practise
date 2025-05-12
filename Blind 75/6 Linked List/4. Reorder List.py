class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head) -> None:

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
        second = slow.next

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
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            
            curr2.next = temp1

            curr1 , curr2 = temp1, temp2
        

        



        



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

obj = Solution()
obj.reorderList(head)