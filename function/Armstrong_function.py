
# Question: Write a Python program to check whether a number is an Armstrong number using a function.

def armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        rem = temp % 10
        total = total + rem ** digits
        temp = temp // 10

    return total == n


num = int(input("Enter a number: "))

if armstrong(num):
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")
