class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Mystack:
    def __init__(self):
        self.head = None    #In stack, head will be our topmost element
        self.size = 0       # Here self refers to a stack. For eg: self.size means stack's size
        
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head   #Poitning new_node.next to Stack's head
        self.head = new_node        #Shifting Stack's head to the new_node
        
        self.size +=1               #Increasing the stack's size

    def pop(self):
        if self.head == None:
            return None
        
        else:
            prev = self.head.data
            self.head = self.head.next

            self.size -= 1

            return prev

    def peek(self):
        if self.head == None:
            print("Empty stack")
            return None
        
        else:
            return self.head.data

    def Stack_size(self):
        return self.size


s = Mystack()

s.push(10)
s.push(20)
s.push(30)

print(s.pop())
print(s.peek())

print(s.size)