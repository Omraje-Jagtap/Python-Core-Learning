# Question: write program to implement the doubly linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insertion at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Display forward
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main program
dll = DoublyLinkedList()

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter data: "))
    dll.insert(data)

print("Doubly Linked List:")
dll.display()
