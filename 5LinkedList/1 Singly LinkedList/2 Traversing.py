class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating node
head= Node(10)
head.next= Node(20)
head.next.next= Node(30)

#===============================
#Printing LinkedList
current = head             #creating a pointer pointing to the 1st Node
while current != None:      #The loop continues as long as current is not None (meaning it hasn't reached the end of the list).
    print(current.data, end= "-> ")
    current= current.next
print("None")
