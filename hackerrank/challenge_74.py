'''Task:

 - You are given a 2-D array with dimensions N X M.
 - Your task is to perform the min function over axis 1 
   and then find the max of that.

Input Format:

 - The first line of input contains the space separated values of N and M.
 - The next N lines contains M space separated integers.

Output Format:

Compute the min along axis 1 and then print the max of that result.

Sample Input:

4 2
2 5
3 7
1 3
4 0

Sample Output:

3

Explanation:

The min along axis 1 = [2,3,1,0]
The max of [2,3,1,0] = 3 

'''


import numpy as np

def min_row_max(array):

    min = array.min(axis=1)

    max = min.max()

    return max 


N,M = map(int,input().split())

array_elements = []

for i in range(N):
    elements = list(map(int, input().split()))
    array_elements.append(elements)

array = np.array(array_elements)

result = min_row_max(array)

print(result)