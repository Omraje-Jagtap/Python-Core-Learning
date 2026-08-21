import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if 1 <= (a and b and c and d) and  (a and b and c and d) <= 1000:
    result = a**b + c**d
    print(result)