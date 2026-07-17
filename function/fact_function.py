# WAF to find the factorial of n. 

def fact(n): #talking the n(number) as a parameter
    fact = 1
    i = 1
    while i<= n:
        fact = fact*i
        i = i+1
    return fact

a = int(input("enter the number:"))

factorial = fact(a) #passing the argument to fun-n
print("factorial=",factorial)
