# Question: Write a Python program to update an element in a tuple.

t = (10, 20, 30, 40, 50)

print("Original tuple:", t)

lst = list(t)

pos = int(input("Enter the position to update: "))
value = int(input("Enter the new value: "))

if 0 <= pos < len(lst):
    lst[pos] = value
    t = tuple(lst)
    print("Updated tuple:", t)
else:
    print("Invalid position")
