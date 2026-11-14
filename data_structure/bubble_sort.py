a = [5, 3, 8, 2, 1]

n = len(a)

for i in range(n):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Sorted array:", a)

