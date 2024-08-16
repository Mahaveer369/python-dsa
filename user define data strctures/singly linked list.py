class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        # Create a new node (car) with the given data
        new_node = Node(data)

        # If the train (linked list) is empty, make the new node the first car
        if not self.head:
            self.head = new_node
        else:
            # Find the last car in the train (linked list)
            current = self.head
            while current.next:
                current = current.next

            # Attach the new car to the end of the train (linked list)
            current.next = new_node

# Create a linked list (train)
train = LinkedList()

# Insert new cars (nodes) into the train (linked list)
train.insert('Car A')
train.insert('Car B')
train.insert('Car C')

# Print the train (linked list)
current = train.head
while current:
    print(current.data)
    current = current.next