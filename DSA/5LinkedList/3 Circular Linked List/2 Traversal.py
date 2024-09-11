class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Method 1
def Traversal1(head):
    if head == None:  #when List is empty
        return None
    
    current = head
    while current.next != head:
        print(current.data, end= "-> ")
        current = current.next
    print(current.data, end= "-> ")   #Printing last node explicitly
    print("Head")

#Method 2 - Preferable
def Traversal2(head):      #TC = O(N)  , SC = O(1)
    if head == None:  #when List is empty
        return None

    print(head.data, end = "-> ")   #Printing head explicitly

    current = head.next
    while current != head:        #Start with the second element and stop when we reach head again.
        print(current.data, end= "-> ")
        current = current.next
    print("head")

#Creating Circular linked List
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = head

#----------------
#Traversal
# head = Traversal1(head)
head = Traversal2(head)