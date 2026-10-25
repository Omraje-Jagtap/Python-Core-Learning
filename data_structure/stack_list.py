# Question: Write a Python program to implement a stack
# using a list with push and pop operations.

def push(stack, value):
    stack.append(value)
    print(value, "added to stack")


def pop_item(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Removed element:", stack.pop())


stack = []

push(stack, 10)
push(stack, 20)
push(stack, 30)

print("Stack:", stack)

pop_item(stack)

print("Stack after pop:", stack)
