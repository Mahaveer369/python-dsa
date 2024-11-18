
class Node:
    """Represents a single node in the linked list."""
    
    def __init__(self, data):
        """
        Initializes a Node with given data.

        Args:
            data (any): Data to be stored in the node.
        """
        self.data = data
        self.next = None


class LinkedList:
    """Represents a linked list data structure."""
    
    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.head = None


    def insert(self, data):
        """
        Inserts a new node with the given data at the end of the linked list.

        Args:
            data (any): Data to be stored in the new node.
        """
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def print_list(self):
        """
        Prints all elements in the linked list.
        """
        current = self.head
        while current:
            print(current.data)
            current = current.next


# Create a linked list
train = LinkedList()

# Insert new nodes into the linked list
train.insert('Ferrari Purosangue')
train.insert('Bently continental GT  ')
train.insert('  BMW  I8 ')

# Print the linked list
train.print_list()  
