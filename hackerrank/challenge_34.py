'''Task:
you are given a list of N lowercase English letters. For a given integer K, 
you can select any K indices (assume -based indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format:
The input consists of three lines. The first line contains the integer N, denoting the length of the list. 
The next line consists of N space-separated lowercase English letters, denoting the elements of the list.
The third and the last line of input contains the integer K, denoting the number of indices to be selected

Output Format:
Output a single line consisting of the probability that at least one of the K indices selected contains the letter:'a'.
Note: The answer must be correct up to 3 decimal places.

Constraints:
1 <= N <= 10
1 <= K <= N
All the letters in the list are lowercase English letters.

Sample Input:
4 
a a c d
2

Sample Output:
0.8333'''

import math

n = int(input())
List = list(map(str, input().split()))
m = int(input())

k = List.count('a')

if 1 <= n <= 10:
    if m > n:
        P = 0.0
    else:
        if k == 0:
            P = 0.0
        else:
            P = 1 - (math.comb(n - k, m) / math.comb(n, m))
    print(round(P, 3))