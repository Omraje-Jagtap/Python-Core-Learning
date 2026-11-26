# Question: Write a Python program to find the sum of even and odd numbers in a list.

numbers = [10, 15, 20, 25, 30, 35]

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
