'''Task:
The reads an integer,n. For all non-negative integers i<n,print i^2.

Input Format
The first and only line contains the integer,n.

Constraints
1 <= n <= 20

Output Format
Print n lines, one corresponding to each i.

Sample Input:
5
Sample Output:
0
1
4
9
16'''


if __name__ == '__main__':
    n = int(input())
    
if n >= 1 and n <=20:
    for i in range(n):
        j = i ** 2
        print(j)
else:
    print("integer must be in 1 to 20")