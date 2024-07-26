class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def show(head):
    current = head
    while current != None:
        print(current.data, end= "-> ")
        current = current.next
    print("None")

#Method 1
def Reverse(head):
    stack = []

    current = head
    while current != None:
        stack.append(current.data)
        current = current.next
    
    current = head
    while current != None:
        current.data = stack.pop()
        current = current.next
    
    return head

def Reverse2(head):
    prev = None
    curr = head

    while curr != None:
        front = curr.next
        curr.next = prev

        prev = curr
        curr = front
    
    return prev
        




head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

show(head)

#==============
#method 1 Reversing a List
head = Reverse2(head)
show(head)
