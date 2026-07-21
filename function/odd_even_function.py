# WAF to print the number is even or odd.

def even_odd(n):
    if(n%2 == 0):
        print("EVEN")
    else:
        print("ODD")

num = int(input("enter the no. to check it is odd or even:"))
even_odd(num)
