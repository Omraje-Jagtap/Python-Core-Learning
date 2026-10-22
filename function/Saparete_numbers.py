# Question: Write a Python program to separate even and odd numbers from a list using a function.

def separate_numbers(numbers):
    even = []
    odd = []

    for n in numbers:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    return even, odd


data = [1, 2, 3, 4, 5, 6]

even, odd = separate_numbers(data)

print("Even numbers:", even)
print("Odd numbers:", odd)
