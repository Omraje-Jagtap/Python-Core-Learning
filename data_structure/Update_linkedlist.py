# Question: write the program to update the value in linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert node at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Update node
    def update(self, pos, new_data):
        temp = self.head
        count = 1

        while temp:
            if count == pos:
                temp.data = new_data
                print("Node updated successfully")
                return

            temp = temp.next
            count += 1

        print("Invalid position")

    # Display linked list
    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Before updating:")
ll.display()

ll.update(2, 100)

print("After updating:")
ll.display()
