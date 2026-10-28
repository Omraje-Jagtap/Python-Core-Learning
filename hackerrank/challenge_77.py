'''Task:

 - You are given a 2-D array with dimensions N X M.
 - Your task is to perform the sum tool over axis 0 and then find the  of that result.

Input Format:

 - The first line of input contains space separated values of N and M.
 - The next N lines contains M space separated integers.

Output Format:

 - Compute the sum along axis 0. Then, print the product of that sum.

Sample Input:

2 2
1 2
3 4

Sample Output:

24

Explanation:

The sum along axis 0 = [4 6]
The product of this sum = 24


'''

import numpy as np

def sum_of_array(array_ele):

    array = np.array(array_ele)
    sum = np.sum(array,axis=0)

    return sum

def product_of_sum(array_ele):

    sum = sum_of_array(array_ele)
    product = np.prod(sum)

    return product


N,M = map(int,input().split())

array_elements = []

for i in range(N):
    elements = list(map(int, input().split()))
    array_elements.append(elements)

result = product_of_sum(array_elements)

print(result)