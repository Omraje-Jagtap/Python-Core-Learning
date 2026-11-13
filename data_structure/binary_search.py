# Question: write the Python program to implement the binary search technique.

import array

a = array.array('i', [10, 20, 30, 40, 50])

n = int(input("Enter element to search: "))

low = 0
high = len(a) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if a[mid] == n:
        print("Element found at index:", mid)
        found = True
        break

    elif n < a[mid]:
        high = mid - 1

    else:
        low = mid + 1

if not found:
    print("Element not found")

