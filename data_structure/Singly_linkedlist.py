# Question: write program for implementation of singly linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Creation of linked list
head = Node(10)

second = Node(20)
third = Node(30)

head.next = second
second.next = third


# Traversal of linked list
temp = head

while temp is not None:
    print(temp.data, end=" -> ")
    temp = temp.next

print("NULL")

