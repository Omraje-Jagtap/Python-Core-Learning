# WAF to check the number is perfect or not.
''' A perfect number is a number that is the sum of all its positive 
    divisior without itself is equal to that number.'''

def perfect(num):
    list = []
    for i in range(1,num):
        if num % i == 0:
            list.append(i)
    if sum(list) == num:
        print("the",num,"is perfect number")
    else:
        print("the",num,"is not perfect number")

try:
    number = int(input("enter the number:"))  
    perfect(number)
except ValueError:
    print("only integers are allowed")
