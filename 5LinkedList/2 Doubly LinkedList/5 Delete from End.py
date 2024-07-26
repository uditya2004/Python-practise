class Node:
    def __init__(self,data):
        self.data= data 
        self.prev = None
        self.next = None

def show(head):
    current = head
    while current != None:
        print(current.data, end= "-> ")
        current = current.next
    print("None")

def DeleteFromEnd(head):
    if head == None:
        return None
    if head.next == None:
        return None
    
    current = head
    while current.next.next != None:
        current = current.next
    
    current.next = None
    return head



head = Node(10)
node2 = Node(20)
node3 = Node(30)

head.next = node2

node2.prev = head
node2.next = node3

node3.prev = node2

show(head)

#=============
#Delete from end
head = DeleteFromEnd(head)
show(head)
