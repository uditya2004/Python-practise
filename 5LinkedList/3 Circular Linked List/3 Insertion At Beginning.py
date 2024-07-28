class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def show(head):
    if head == None:
        return None
    
    print(head.data, end="-> ")

    current = head.next
    while current != head:
        print(current.data, end="-> ")
        current = current.next
    print("Head")
    return head

#Method 1 - TC: O(N), SC: O(1)
def InsertAtBeg(head,data):
    new_node = Node(data)

    if head == None:
        new_node.next = new_node
        return new_node
    
    else:
        currrent = head
        while currrent.next != head:
            currrent = currrent.next
        
        currrent.next = new_node
        new_node.next = head
        return new_node

#Method 2 - Constant Time (Tricky Solution)
def InsertAtbeg2(head,data):
    if head == None:
        new_node.next = new_node
        return new_node
    
    else: 
        new_node = Node(data)       #creating new Node  

        #We insert new node after head and then swap data of head and new node
        new_node.next = head.next   #First do this , so we don't loose link of current 2nd node
        head.next = new_node
        head.data, new_node.data = new_node.data, head.data  #swapping data 

        return head
    

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head

show(head)

#-----------
#Insert At the head
head = InsertAtbeg2(head, 50)
show(head)