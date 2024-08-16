class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def print_list(self):
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break

# Create a circular linked list
cll = CircularLinkedList()

# Append nodes to the list
cll.append(1)
cll.append(2)
cll.append(3)

# Print the list
cll.print_list()