class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            return None
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return self
    
    def pop(self):
        if self.length == 0:
            return None
        
        popped_value = self.top.value
        if self.length == 1:
            self.top = None
            self.bottom = None
        else:
            self.top = self.top.next
        self.length -= 1
        return popped_value

stack = Stack()
stack.push('google')
stack.push('udemy')
stack.push('discord')
print(stack.peek())
print(stack.pop())
print(stack.peek())