class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):  # list1 and list2 are the heads of the two list
        dummy = ListNode(-1)
        curr = dummy

        l1 = list1
        l2 = list2

        while l1 != None and l2 != None:

            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next

        while l1 != None:
            curr.next = l1
            l1 = l1.next
            curr = curr.next

        while l2 != None:
            curr.next = l2
            l2 = l2.next
            curr = curr.next

        return dummy.next





list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

merged = Solution()
merged = merged.mergeTwoLists(list1, list2)