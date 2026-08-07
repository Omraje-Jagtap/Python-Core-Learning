'''Task:
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric 
difference indicates those values that exist in either M or N but do not exist in both.

Input Format:
The first line of input contains an integer,M.
The second line contains N space-separated integers.
The third line contains an integer, M.
The fourth line contains N space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.

Sample Input:

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

Sample Output:

5
9
11
12
'''

def symmetric_diff(set1,set2):
    diff = set1.symmetric_difference(set2)

    return sorted(diff)


len1 = int(input())
M = set(map(int,input().split()))
len2 = int(input())
N = set(map(int, input().split()))

result = symmetric_diff(M,N)

for i in result:
    print(i)

