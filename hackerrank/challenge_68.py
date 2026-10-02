'''Task:

 - You are given three integers: a, b, and m. Print two lines.
 - On the first line, print the result of pow(a,b). On the second line, 
   print the result of pow(a,b,m).

Input Format:

 - The first line contains a, the second line contains b, and the third line contains m.

Constraints:

 - 1 <= a <= 10
 - 1 <= b < =10
 - 2 <= m <= 1000

Sample Input:

3
4
5

Sample Output:

81
1

'''


def mod(a,b,m):
    result = []
    pow_1 = (pow(a, b))
    pow_2 = (pow(a, b, m))

    return pow_1,pow_2

a = int(input())
b = int(input())
m = int(input())


result1,result2 = mod(a,b,m)

print(result1)
print(result2)
