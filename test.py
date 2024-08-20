class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def show(head):
    curr = head
    while curr != None:
        print(curr.data,end = "-> ")
        curr = curr.next
    print("None")

def DeleteFromBeg(head):
    if head == None:
        return head
    else:
        return head.next

def DeleteFromEnd(head):
    if head == None:
        return None
    if head.next == None:
        return None

    curr = head
    while curr.next.next != None:
        curr = curr.next
    curr.next = None
    return head

def DeleteAtPosition(head, position):
    if head == None:
        return None
    
    if position <=0:
        return None
    
    curr = head
    for i in range(0,position-2):
        curr = curr.next

        if curr == None:
            return head
    
    curr.next = curr.next.next
    return head

#DRIVER CODE
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
show(head)

head = DeleteAtPosition(head, 9)
show(head)

