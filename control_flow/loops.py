# problem solving to understand the while loop.

# WAP to to search the number in tuple.

tup = (1,2,3,4,5,5,6,7,8,9,0)
i = 0
x = int(input("enter the no. :"))

while i < len(tup):
    if(tup[i]==x):
        print("found",i)
    i = i+1


# find the sum of first n natural number.

i = 1
a = int(input("enter the no. :"))
sum =0
while i<=a:
    sum = sum + i
    i = i+1

print("the sum of first",a,"natural numbers is:",sum)