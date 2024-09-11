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

def DeleteFromBeg(head):
    if head == None:
        return None
    
    elif head.next == head:
        return None
    
    else:
        head.data = head.next.data
        head.next= head.next.next

        return head
    

def DeleteAtposition(head, postion):
    if postion == 1:
        return DeleteFromBeg(head)
    
    else:
        current = head
        for i in range(0,postion-2):
            current = current.next
        
        current.next = current.next.next

        return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

show(head)

#--------------
#Delete Kth Node
head = DeleteAtposition(head, 1)
show(head)