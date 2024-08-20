class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def show(head):
    current = head       #Starting with the object passed i.e head
    while current != None:
        print(current.data, end= "-> ")
        current = current.next
    print("None")

def DeleteFromBeginning(head):          #TC: O(1), SC: O(1)
    if head == None:   
        return None
    else:                   #We just have to move the head. Deallocating memory is taken care by Python
        return head.next
    
def DeleteFromEnd(head):
    if head == None:   #Empty Linked List
        return None
    
    if head.next == None:  #List with single element
        return None
    
    current = head
    while current.next.next !=None:
        current = current.next
    
    current.next = None
    return head
    
def DeleteFromPosition(head, position):
    current = head
    for i in range(0,position-2):
        current = current.next
    
    current.next = current.next.next
    return head
    
def DeleteBeforePosition(head, position):
    if head == None or position <= 0:
        return None
    
    else: 
        current = head
        for i in range(0,position-3):
            current = current.next
        
        current.next = current.next.next
        return head
    
def DeleteAfterPosition(head, position):
    if head == None or position <= 0:
        return None
    
    else:
        current = head
        for i in range(0,position-1):
            current = current.next
        
        if current.next != None and current.next.next != None:
            current.next = current.next.next
        else:
            current.next = None
        return head




#Creating Linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
head.next.next.next.next.next = Node(60)


print("Original: ",end = " ")
show(head)

#--------------------------
#Deletion from the beginning
print("\nDelete from the beginning")
head = DeleteFromBeginning(head)
show(head)

#--------------------------
#Deletion from the End
print("\nDelete from the End")
head = DeleteFromEnd(head)
show(head)

#--------------------------
#Deletion from the Postion
print("\nDelete from the Postion")
head = DeleteFromPosition(head, 2)
show(head)

#--------------------------
#Deletion before position
print("\nDelete before positon")
head = DeleteBeforePosition(head, 3)
show(head)

#--------------------------
#Deletion After position
print("\nDelete after position")
head = DeleteAfterPosition(head, 2)
show(head)