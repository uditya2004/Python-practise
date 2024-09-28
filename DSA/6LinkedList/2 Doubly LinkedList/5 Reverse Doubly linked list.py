class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def show(head):
    current  = head 
    while current != None:
        print(current.data, end= "-> ")
        current = current.next
    print("None")

def Reverse(head):
    if head == None:
        return None
    
    if head.next == None:
        return head
    
    current = head
    prev = None
    while current != None:
        prev = current                #Storing the current everytime before moving "current" to next , so at last, "current" will become None and last element becomes "prev" , which we will return.
        current.prev, current.next = current.next, current.prev      #Swapping
        current = current.prev            #As next and prev is swapped , so If we have to move to next element we will use "current.prev"
    return prev

#Creating Nodes
head = Node(10)
node2 = Node(20)
node3 = Node(30)

#Linking Nodes
head.next = node2

node2.prev = head
node2.next = node3

node3.prev = node2

show(head)

#=================
#Reverse Linked list
head = Reverse(head)
show(head)


