#DOUBT - CODE COPIED FROM CHATGPT - LEARN THIS TOPIC


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity         # Set the capacity of the Stack
        self.stack = [None] * capacity  # The list is of fixed size, equal to the capacity c of the queue, and is initially filled with None to indicate that the positions in the list are empty. So, if c is 4, the expression [None] * c will result in [None, None, None, None].
        self.top = -1        

    def push(self, element):
        if self.top == self.capacity - 1:
            print("Stack Overflow! Cannot add element:", element)
        else:
            self.top += 1
            self.stack[self.top] = element
            print(f"Element {element} pushed to stack.")

    def pop(self):
        if self.top == -1:
            print("Stack Underflow! No element to pop.")
            return None
        else:
            popped_element = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"Element {popped_element} popped from stack.")
            return popped_element

    def peek(self):
        if self.top == -1:
            print("Stack is empty. No element to peek.")
            return None
        else:
            print(f"Element on top of the stack is {self.stack[self.top]}.")
            return self.stack[self.top]

    def size(self):
        print(f"Current stack size is {self.top + 1}.")
        return self.top + 1

# Create a stack with a capacity of 5
stack = Stack(5)

# Perform stack operations
stack.push(10)
stack.push(20)
stack.push(30)
stack.peek()  # Should return 30
stack.pop()   # Should remove 30
stack.size()  # Should return 2
stack.pop()   # Should remove 20
stack.pop()   # Should remove 10
stack.pop()   # Should indicate stack underflow
