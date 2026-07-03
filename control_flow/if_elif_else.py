# WAP to check if a nnumber is entered by user is odd or even

num = int(input("enter the number:"))

if(num % 2 == 0):
    print("the number is even")
else:
    print("number is odd")



# WAP to find the greatest of three number enter by user.

a = int(input("enter three numbers:"))
b = int(input("enter three numbers:"))
c = int(input("enter three numbers:"))

if(a > b and a > c):
    print(a,"the a numberis greatest")
elif( b > a and b > c):
    print("the",b,"is greatest number:")
else:
    print(c,"is greatest number")