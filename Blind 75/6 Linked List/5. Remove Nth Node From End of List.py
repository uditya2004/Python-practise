class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Method 1:- Better solution (Require 2 pass)
    # def removeNthFromEnd(self, head, n: int):

    #     if head == None or head.next == None: 
    #         return None

    #     #findinng the length of the linked list.  TC: O(N)
    #     length = 0
    #     curr = head
    #     while curr != None:
    #         length +=1
    #         curr = curr.next
        
    #     # deleting the node.   TC: O(M)
    #     target = (length - n) + 1   #4

    #     if target == 1:   # case of delete from beginning
    #         return head.next

    #     curr1 = head
    #     for i in range(0, target-2):  
    #         curr1 = curr1.next
        
    #     curr1.next = curr1.next.next

    #     return head
        
    #Method 2:- Best Solution (Single Pass)
    """
    APPROACH
    1. Create 2 pointers -> left and right
    2. Left pointer points to the dummy node "0".
    2. Move the "right" pointer "n" steps ahead of the left pointer
    3. Now move both the pointer simultaneously one step at a time until "right" reaches "None". When "right" reaches "None", left pointer will reach one node behind the target node.
    4. Delete the target node.
    """
    def removeNthFromEnd(self, head, n: int): 
        dummy = ListNode(0, head)       # The dummy node handles edge cases like removing the head.
        left = dummy
        right = head
        
        #move the 2nd pointer n steps ahead
        while n > 0 and right != None:  # 2 -> 1 
            right = right.next
            n -=1
        
        # move both the pointers ahead simultaneously until the 2nd pointer's next "None". When the 2nd pointer's next reaches "None", 1st pointer is one node behind the target node (node to delete)
        while right != None:
            left = left.next
            right = right.next
        
        # deleting the target node:
        left.next = left.next.next

        return dummy.next

    def printing(self,head):
        curr = head
        while curr != None:
            print(f'{curr.val} -> ', end = ' ')
            curr = curr.next
        print('None')

"""
this example is having error
"""
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

obj = Solution()
head = obj.removeNthFromEnd(head, 2)
obj.printing(head)