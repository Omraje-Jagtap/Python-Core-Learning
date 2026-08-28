'''Task:
You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on).
You are required to sort the data based on the Kth attribute and print the final resulting table.
Follow the example given below for better understanding.

Note that K is indexed from 0 to M-1, where M is the number of attributes.

Note: 
If two attributes are the same for different rows, for example,
if two atheletes are of the same age, print the row that appeared first in the input.

Input Format:

The first line contains N and M separated by a space.
The next M lines each contain M elements.
The last line contains K.

Constraints:

1 <= N,M <= 1000
0 <= k <= M
each element <= 1000

Output Format:

Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input:

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

Sample Output:

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

'''

def sorting(table, k):
    sorted_table = sorted(table, key=lambda row: row[k])
    return sorted_table

N, M = map(int, input().split())

lists = []
for _ in range(N):
    user_input = list(map(int, input().split()))
    lists.append(user_input)


K = int(input())


result = sorting(lists, K)

for row in result:
    print(*row)


''' ----- the another same code using the pandas library -----'''

# import pandas as pd

# N,M = map(int,input().split())

# lists = []
# for i in range(N):
#     user_input = list(map(int, input().split()))
#     lists.append(user_input)

# K =  int(input())

# df = pd.DataFrame(lists)
# sorted_lists = sorted(lists, key=lambda row: row[K])
# for i in sorted_lists:
#     print(*i)
    