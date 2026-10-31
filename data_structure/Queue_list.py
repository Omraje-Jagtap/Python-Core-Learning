# Question: Write a Python program to implement a queue
# using a list.

def enqueue(queue, value):
    queue.append(value)


def dequeue(queue):
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Removed element:", queue.pop(0))


queue = []

enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)

print("Queue:", queue)

dequeue(queue)

print("Queue after removal:", queue)
