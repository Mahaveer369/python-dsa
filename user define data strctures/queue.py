# Initialize an empty queue
queue = []

# Define a function to enqueue an element
def enqueue():
    element = input("Enter the element: ")
    queue.append(element)
    print("Queue:", queue)

# Define a function to dequeue an element
def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        dequeued_element = queue.pop(0)
        print("Dequeued element:", dequeued_element)

# Main program loop
while True:
    print("\nSelect the operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        break
    else:
        print("Invalid operation! Please try again.")
