class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def show(self):
        current = head
        while current != None:
            print(current.data , end= "-> ")
            current = current.next
        print("None")
    
    def SortedInsert(self, data):
        new_node = Node(data)
        if head == None:                   #If list is empty , then we make the new node head
            return new_node

        elif data < head.data :
            new_node.next = head
            return new_node
        
        else:
            j= head
            while j.next != None and j.next.data < data:
                j = j.next

            new_node.next = j.next
            j.next = new_node
            return head

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

head.show()

#==========================
#Insert an element in a position so that list remain sorted
head = head.SortedInsert(1)
head.show()