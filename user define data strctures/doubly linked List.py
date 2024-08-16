class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Create a doubly linked list
dll = DoublyLinkedList()

# Append nodes to the list
dll.append(1)
dll.append(2)
dll.append(3)

# Prepend nodes to the list
dll.prepend(0)
dll.prepend(-1)

# Print the list
dll.print_list()