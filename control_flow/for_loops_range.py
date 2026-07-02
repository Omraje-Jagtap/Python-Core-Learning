# problem solving to understand the for loop and range() function.


# print the numbers frim 1 to 100 and 100 to 1.

for n in range(1,101):
    print(n) # 1 to 100



i = 100
while i>=0:
    print(i) # 100 to 1
    i =i-1

for n in range(100,0,-1):
    print(n)



# multiplication table of n numbers.

a = int(input("entre the number:"))

for n in range(1,11):
    print(a*n)



# find factorial of n numbers.

a = int(input("enter the No: "))
fcat = 1
for n in range(1,a+1):
    fcat = fcat*n

print("the factorial of",a,"is: ",fcat)


#print the sum of all even numbers in to 100.
sum = 0
for n in range(2,101,2):
    print(n)
    sum = sum + n

print(sum)


# fibonacci series.

a =0 
b = 1
c = 0

for n in range(1,15):
    c= a+b
    print(c)
    a = b
    b = c


# prime number checker. 

a = int(input("enter the number to check the it is prime or not:"))
flag =0
for n in range(2,a):
    if(a%n == 0):
      
      flag = 1

if(flag == 1):
    print("not prime")
else:
    print("prime")



# the collatz conjectrue
'''take a positive integer n write a loop that follows these two rules until n becomes 1
      i) if n is even, the next number is n/2
      ii) if n is odd then next number is 3n+1                             '''

n = int(input("enter the number:"))
i = 1

while i > 0:
    if(n%2==0):
        n = n/2
        print(n)
    elif(n%2 != 0):
        n = 3*n+1
        print(n)
    if(n == 1):
        break
    else: i =i+1



# The digit extractor.(the reverse the number)

n = int(input("enter the number that you want to reverse"))

r = 0
while n > 0:
    r= n%10
    print(r)
    n = n//10




