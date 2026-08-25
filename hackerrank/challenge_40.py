'''Task:
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format:

The first line will contain the number of test cases, T.
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set B.
The third line of each test case contains the number of elements in set A.
The fourth line of each test case contains the space separated elements of set B.

Constraints:

0 < T < 21
0 < total no in each set < 1001

Output Format:
Output True or False for each test case on separate lines.

Sample Input:

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

Sample Output:

True 
False
False

'''

T = int(input())

list = []
for i in range(T):
    no_of_elements1 = int(input())
    elements1 = set(map(int, input().split()))
    no_of_elements2 = int(input())
    elements2 = set(map(int, input().split()))

    if (0 < T < 21) and (0 < (len(elements1) and len(elements2)) < 1001):
        if elements1.issubset(elements2):
            list.append(True)
        else:
            list.append(False)

for i in list:
    print(i)