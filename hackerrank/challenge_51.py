'''
Task:
 - Given a list of rational numbers,find their product.

Input Format:

 - First line contains n, the number of rational numbers.
 - The ith of next n lines contain two integers each, 
   the numerator(Ni) and denominator (Di) of the ith rational number in the list.

Constraints:

 - 1 <= n <= 100
 - 1 <=  Ni , Di <= 10^9

Output Format:

 - Print only one line containing the numerator and denominator of the product of the numbers in 
   the list in its simplest form, i.e. numerator and denominator have no common divisor other than 1.

Sample Input:

3
1 2
3 4
10 6

Sample Output:

5 8 

Explanation:

Required product is 1/2 . 3/4 . 10/6 = 5/8

'''




from fractions import Fraction
from functools import reduce

def product(fracs):
    if 1 <=  len(fracs) <= 100:
        for f in fracs:
            if not (1 <= f.numerator <= 10**9 and 1 <= f.denominator <= 10**9):
                raise ValueError("Numerator and denominator must be between 1 and 10^9")
        t =  reduce(lambda x, y: x * y, fracs)
        return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)



# this program is woking without the any module importing

# Remove the comments form the Code to use it.

'''import math

def product(num_list):
    denominator = 1
    numarator = 1
    for i in range(len(num_list)):
        denominator = denominator * num_list[i][0]
        numarator = numarator * num_list[i][1]

    gcd = math.gcd(numarator,denominator)
    denominator = denominator // gcd
    numarator = numarator // gcd
    return denominator,numarator



n = int(input())

numbers = []
for i in range(n):
    a,b = (map(int , input().split()))
    numbers.append([a,b])

result = product(numbers)
print(*result)

'''