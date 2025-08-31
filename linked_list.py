class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # Create the head node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # Create a new node
        new_node = Node(value)
        print(new_node.value)  # printing like console.log

        # Attach it to the tail
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return self

    # prepend a node to the beginning of the list
    def prepend(self, value):
        new_node = Node(value)
        print(new_node.value)

        # Attach it to the head
        new_node.next = self.head
        self.head = new_node
        self.length += 1
        return self
    
    # insert a node at a specific index
    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        leader = self.head 
        i = 0 
        while i < index - 1:
            leader = leader.next
            i += 1
        
        holding_pointer = leader.next
        leader.next = new_node
        new_node.next = holding_pointer
        self.length += 1
        return self
    
    def remove(self, index):
        leader = self.head
        i = 0
        while i < index - 1:
            leader = leader.next
            i += 1
        leader.next = leader.next.next
        leader.next.next = None
        self.length -= 1
        return self
      

    # print the list
    def print_list(self):
        array = []
        current_node = self.head
        while current_node is not None:
            array.append(current_node.value)
            current_node = current_node.next
        print(array)
        return array
    
# Doubly Linked List
class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
        return self
    
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1
        return self
    
    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        if index == 0:
            return self.prepend(value)
        new_node = Node(value)
        leader = self.head
        follower = leader.next
        i = 0
        while i < index - 1:
            leader = leader.next
            i += 1
        follower = leader.next
        leader.next = new_node
        new_node.prev = leader
        new_node.next = follower
        follower.prev = new_node
        self.length += 1
        return self
    
    def remove(self, index):
        leader = self.head
        i = 0
        while i < index - 1:
            leader = leader.next
            i += 1
        leader.next = leader.next.next
        leader.next.next = None
        self.length -= 1
        return self
    
 
    def reverse(self):
        if not self.head or not self.head.next:
            return self
        
        current = self.head
        self.tail = self.head  # old head will become new tail
        
        while current:
            # swap next and prev
            current.prev, current.next = current.next, current.prev
            # move to the "next" node (which is the old prev)
            current = current.prev
        
        # after loop, current is None, but the last valid node is self.tail.prev
        self.head = self.tail.prev
        return self




# Usage
my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.insert(2, 99)
my_linked_list.insert(20, 88)
my_linked_list.remove(2)
my_linked_list.print_list()
