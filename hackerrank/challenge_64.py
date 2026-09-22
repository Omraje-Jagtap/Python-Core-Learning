'''Task:

 - You are given two integer arrays, A and B of dimensions N X M.
 - Your task is to perform the following operations:

1. Add ( + )
2. Subtract ( - )
3. Multiply ( * )
4. Integer Division ( / )
5. Mod ( % )
6. Power ( ** )

Note:

 - There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

Input Format:

 - The first line contains two space separated integers, N and M.
 - The next N lines contains M space separated integers of array A.
 - The following N lines contains M space separated integers of array B.

Output Format:

 - Print the result of each operation in the given order under Task.

Sample Input:

1 4
1 2 3 4
5 6 7 8

Sample Output:

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 

Use // for division in Python 3.

'''


import numpy as np

def operations(arr1, arr2):
    operation = []
    operation.append(arr1 + arr2)
    operation.append(arr1 - arr2)
    operation.append(arr1 * arr2)
    operation.append(arr1 // arr2)
    operation.append(arr1 % arr2)
    operation.append(arr1 ** arr2)
    return operation


N, M = map(int, input().split())

A_array = []
for _ in range(N):
    row = list(map(int, input().split()))
    A_array.append(row)

B_array = []
for _ in range(N):
    row = list(map(int, input().split()))
    B_array.append(row)


A_array = np.array(A_array).reshape(N, M)
B_array = np.array(B_array).reshape(N, M)

result = operations(A_array, B_array)

for i in result:
    print(i)

