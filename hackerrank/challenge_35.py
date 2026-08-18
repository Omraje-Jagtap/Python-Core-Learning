'''Task:
You are given a function f(x) = x^2. You are also given K lists. The ith list consists of Ni elements.
You have to pick one element from each list so that the value from the equation below is maximized:
S = (f(X1)+ f(X2) + f(Xk))% M

Xi denotes the element picked from the ith list. Find the maximized value Smax obtained.
% denotes the modulo operator.

 - Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements
   and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format:
The first line contains 2 space separated integers K and M.
The next K lines each contains an integer Ni, denoting the number of elements in the ith list,
followed by Ni space separated integers denoting the elements in the list.

Constraints:
1 <= K <= 7
1 <= M <= 1000
1 <= Ni <= 7
1 <= magnitude of the elements in list <= 10^9

Output Format:
Output a single integer denoting the value Smax.

Sample Input:

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output:
206
'''

from itertools import product

K, M = map(int, input().split())
lists = []

for _ in range(K):
    data = list(map(int, input().split()))
    Ni = data[0]
    elements = data[1:]

    if not (1 <= Ni <= 7):
        raise ValueError("Ni must be between 1 and 7")

    for ele in elements:
        if not (1 <= ele <= 10**9):
            raise ValueError("Element must be between 1 and 10^9")

    lists.append(elements)

if (1 <= K <= 7) and (1 <= M <= 1000):
    max_val = 0
    for combo in product(*lists):   
        total = sum(x*x for x in combo)
        remainder = total % M
        max_val = max(max_val, remainder)

    print(max_val)
else:
    raise ValueError("K must be between 1 and 7, M between 1 and 1000")

