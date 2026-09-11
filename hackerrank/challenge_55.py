'''Task:

You are given two integer arrays of size N X P and M X P (N & M are rows, and P is the column). 
Your task is to concatenate the arrays along axis 0.

Input Format:

The first line contains space separated integers N,M and P.
The next N lines contains the space separated elements of the P columns.
After that, the next M lines contains the space separated elements of the P columns.

Output Format:

 - Print the concatenated array of size (N + M) X P.

Sample Input:

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
Sample Output:

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
 
 '''


import numpy as np

X, N, M = map(int, input().split())

array1 = [list(map(int, input().split())) for _ in range(X)]

array2 = []
try:
    while True:
        row = input().strip()
        if not row:
            break
        array2.append(list(map(int, row.split())))
except EOFError: # beacause of the on hackerrannk gives error.
    pass

arr1 = np.array(array1)
arr2 = np.array(array2)

print(np.concatenate((arr1, arr2), axis=0))
