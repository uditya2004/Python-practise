class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
def show(head):
    current = head
    while current != None:
        print(current.data, end= "-> ")
        current = current.next
    print("None")
    

def InsertAtBeg(head,data):
    new_node = Node(data)
    
    if head != None:        # If head is initally None , then we don't access it's prev
        head.prev = new_node

    new_node.next = head
    return new_node

def InsertAtEnd(head,data):
    new_node = Node(data)
    if head == None:
        return new_node
    else:
        current = head
        while current.next != None:
            current = current.next
        
        new_node.prev = current
        current.next = new_node
        return head
    
head = None   #Assuming empty linked list

#-----------------------
print("\nInsert at the beginning")
head = InsertAtBeg(head, 10)
head = InsertAtBeg(head, 20)
show(head)

#------------------------------
print("\nInsert a the end")
head = InsertAtEnd(head, 60)
head = InsertAtEnd(head, 90)
show(head)
