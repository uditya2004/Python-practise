class Node:
    def __init__(self,data ):
        self.data = data
        self.next = None

def show(head):
    if head == None:
        print("None")
        return None
    
    else:
        print(head.data, end="-> ")
        current = head.next
        while current != head:
            print(current.data, end="-> ")
            current = current.next
        print("Head")

#Method 1- TC: O(N) , SC: O(1)
def DeleteFromBeg1(head):
    if head == None:
        return None
    
    elif head.next == head:
        return None
    
    else:
        current = head
        while current.next != head:
            current = current.next
        
        current.next = head.next

        return head.next
    
#Method 2- TC: O(1) , SC: O(1)
def DeleteFromBeg2(head):
    if head == None:
        return None
    
    elif head.next == head:
        return None
    
    else: 
        head.data = head.next.data   #Copying the data of 2nd node in the head
        head.next = head.next.next   #Seting the link of the head node with the 3rd node.

        return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

show(head)

#----------------
#Delete From Beginning
head  = DeleteFromBeg2(head)
show(head)