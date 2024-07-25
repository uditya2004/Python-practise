class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def show(self):
        current = head
        while current != None:
            print(current.data , end= "-> ")
            current = current.next
        print("None")

    #Method 1 - Using Stack
    def Reverse1(self):
        stack = []
        current = head

        # Pushing all the elements to a stack
        while current != None:   
            stack.append(current.data)
            current = current.next
        
        #Poping elements from stack and putting into linked list
        current = head
        while current != None: 
            current.data = stack.pop()
            current = current.next
        
        return head
    
    #Method 2 - Changing Links of Node
    def Reverse2(self):
        curr = head
        prev = None
        #Node before "curr" -> prev,  Node after "curr" -> front.

        while curr is not None:      # We move till current pointer reaches end.
            front = curr.next        #Before changing the pointer to point to prev node , we store the address of front node, else we would lost the address of front element
            curr.next = prev         #We change the pointer to point to previous node
            prev = curr              # First move prev pointer forward, so we don't lost address of curr node
            curr = front             # Then move curr pointer forward
        
        return  prev            
        



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head.show()

#=======================
# Reverse the Linked List

#Method 1 = We Push all the elements to a stack, then Pop elements and putting into linked list
# head = head.Reverse1()       #TC = O(N) , SC = O(N)
# head.show()

#------------------
#Method 2 (More efficient)
head = head.Reverse2()       #TC = O(N) , SC = O(1)
head.show()