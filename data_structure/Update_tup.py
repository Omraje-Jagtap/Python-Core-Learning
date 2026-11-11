# Question: Write a Python program to update an element in a tuple.

data = (10, 20, 30, 40, 50)

print("Original tuple:", data)

lst = list(data)

pos = int(input("Enter position to update: "))
value = int(input("Enter new value: "))

if 0 <= pos < len(lst):
    lst[pos] = value
    data = tuple(lst)
    print("Updated tuple:", data)
else:
    print("Invalid position")
