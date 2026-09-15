'''Task:

 - You are given a square matrix A with dimensions N X N. Your task is to find 
   the determinant. 
   
 - Note: Round the answer to 2 places after the decimal.

Input Format:

 - The first line contains the integer N.
 - The next N lines contains the N space separated elements of array A.

Output Format:

 - Print the determinant of A.

Sample Input:

2
1.1 1.1
1.1 1.1

Sample Output:

0.0

'''


import numpy as np

def daterminant(arrayele):

    array = np.array(arrayele)
    determinant = np.linalg.det(array)
    result = np.around(determinant,2)

    return result


N = int(input())

array_ele = []

for i in range(N):
    elements = list(map(float, input().split()))
    array_ele.append(elements)

result = daterminant(array_ele)
print(result)

