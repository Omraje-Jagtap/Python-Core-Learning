'''Task:

 - You are given a 2-D array of size N X M.

 - Your task is to find:
    
    1. The mean along axis 1
    2. The var along axis 0
    3. The std along axis None

Input Format:

 - The first line contains the space separated values of N and M.
 - The next N lines contains M space separated integers.

Output Format:

 - First, print the mean.
 - Second, print the var.
 - Third, print the std.

Sample Input:

2 2
1 2
3 4

Sample Output:

[ 1.5  3.5]
[ 1.  1.]
1.11803398875

'''


import numpy as np

def mean(array_data):

    mean = array_data.mean(axis=1)

    return mean

def variance(array_data):

    var = array_data.var(axis=0)
    
    return var

def standard_deviation(array_data):

    SD = array_data.std()

    return SD

N,M = map(int,input().split())

array_elements = []

for i in range(N):
    elements = list(map(int, input().split()))
    array_elements.append(elements)

array = np.array(array_elements)

result1 = mean(array)
result2 = variance(array)
result3 = standard_deviation(array)

print(result1)
print(result2)

if result3.is_integer():
    print(f"{result3:.1f}")
else:
    print(f"{result3:.11f}")