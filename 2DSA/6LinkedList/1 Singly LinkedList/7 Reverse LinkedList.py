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
def Reverse1(head):
    stack = []
    current = head

    # 1st traversal:- Pushing all the elements to a stack
    while current != None:   
        stack.append(current.data)
        current = current.next
    
    # 2nd Traversal:- Poping elements from stack and overwriting elements of linked list
    current = head
    while current != None: 
        current.data = stack.pop()
        current = current.next
    
    return head
    
#Method 2 - Changing Links of Node
def Reverse2(head):
    curr = head
    prev = None
    #Node before "curr" -> prev,  Node after "curr" -> front.

    while curr is not None:      # We move till current pointer reaches end.
        front = curr.next        #Before changing the pointer to point to prev node , we store the address of front node, else we would lost the address of front element
        curr.next = prev         #We change the pointer to point to previous node
        prev = curr              # First move prev pointer forward, so we don't lost address of curr node
        curr = front             # Then move curr pointer forward
    
    return  prev                # curr and front will become NONE at the end and the prev will point to the last node , which is our required new head
    



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

show(head)

#=======================
# Reverse the Linked List

#Method 1 = We Push all the elements to a stack, then Pop elements and putting into linked list
# head = Reverse1(head)       #TC = O(N) , SC = O(N)
# show(head)

#------------------
#Method 2 (More efficient)
head = Reverse2(head)       #TC = O(N) , SC = O(1)
show(head)


#------------------
#Method 3 Recursively reverse Linked list

#TO DO