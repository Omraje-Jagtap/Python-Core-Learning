# this program is print the multiplication of given numbers using function.

def multiplcation(list):
    p =1
    for m in list:
        p = p*m
    return p

a = input("enter the number with space:")
b = a.split(" ")
print(b)

num =[]

for n in b:
    integer = int(n)
    num.append(integer)

print(num)
mul=multiplcation(num)
print(mul)