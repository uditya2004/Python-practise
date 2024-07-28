class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Mystack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        
        self.size +=1

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

    def size(self):
        return self.size


s = Mystack()

s.push(10)
s.push(20)
s.push(30)

print(s.pop())
print(s.peek())

print(s.size)