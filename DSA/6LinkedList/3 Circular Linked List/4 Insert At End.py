class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def show(head):
    if head == None:
        return None
    
    print(head.data, end="-> ")
    current = head.next
    while current != head:
        print(current.data, end= "-> ")
        current= current.next
    print("Head")

#Method 1 - TC: O(N), SC: O(1)
def InsertAtEnd1(head, data):

    new_node = Node(data)

    if head == None:
        new_node.next = new_node
        return new_node

    else:
        current = head
        while current.next != head:
            current = current.next

        current.next = new_node
        new_node.next = head
        return head

#Method 2  - TC: O(1), SC:O(1)
def InsertAtEnd2(head, data):

    new_node = Node(data)

    if head == None:
        new_node.next = new_node
        return new_node
    
    else: 
        #Inserting after head and swapping data of head and new node
        new_node.next = head.next
        head.next = new_node
        
        head.data, new_node.data = new_node.data, head.data     #Swapping data

        return new_node   #new_node will be the new head


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

show(head)

#=============
#Insert at End
head = InsertAtEnd2(head, 50)
show(head)