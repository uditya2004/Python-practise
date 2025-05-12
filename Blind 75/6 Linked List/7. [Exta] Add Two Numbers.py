# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # Better solution
    # TC: O(6N)
    # SC: O(1)
    # def addTwoNumbers(l1, l2):
    #     str1 = ""
    #     str2 = ""

    #     # copying l1 to str1.   TC: O(N)
    #     curr1 = l1
    #     while curr1 != None:
    #         str1 = str1 + str(curr1.val)
    #         curr1 = curr1.next

    #     # copying l2 to str2.   TC: O(N)
    #     curr2 = l2
    #     while curr2 != None:
    #         str2 = str2 + str(curr2.val)
    #         curr2 = curr2.next
        
    #     # reversing both the strings.   TC: O(2N)
    #     str1 = str1[::-1]
    #     str2 = str2[::-1]

    #     #adding both
    #     result = str(int(str1) + int(str2))

    #     #reversing the result.   TC: O(N)
    #     result = result[::-1]

    #     # creating nodes.   TC: O(N)
    #     dummy = ListNode(-1)
    #     curr = dummy
    #     for i in result:
    #         curr.next = ListNode(int(i))
    #         curr = curr.next
        
    #     return dummy.next
    
    #=======================================
    # Method 2 :- Best Solution
    def addTwoNumbers(l1, l2):
        """
        1. Place pointers on the head of both the lists.
        2. Create a dummy node as temp linked list to store addition resultant linked list.
        3. Add the value of the node at both pointers and create the node next to dummmy node.
        
        """
        # TC: O(max(M, N))
        # SC: O(1)
        curr1 = l1
        curr2 = l2

        dummy = ListNode(-1)
        res = dummy

        carry = 0
        while curr1 != None or curr2 != None or carry !=0:
            v1 = curr1.vaal if curr1 else 0    # if curr1 is None then take value as 0 , otherwise curr1.val
            v2 = curr2.vaal if curr2 else 0    # if curr2 is None then take value as 0 , otherwise curr2.val

            # getting the sum
            add = carry + v1 + v2
            
            # create a node from the sum and adding it to the Dummy Linked List
            res.next = ListNode(add % 10)

            # updating the carry
            carry = add // 10
            
            curr1 = curr1.next if curr1 else None  #if the curr1 is None, then we again to value None only (edge case:- when one list is over while in other some element is left)
            curr2 = curr2.next if curr2 else None
            res = res.next
        

        # returning the head of the answer linked list
        return dummy.next




        




