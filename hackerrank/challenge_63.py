'''Task:

 - You are given a space separated list of nine integers. 
   Your task is to convert this list into a 3 X 3 NumPy array.

Input Format:

 - A single line of input containing 9 space separated integers.

Output Format:

 - Print the 3 X 3 NumPy array.

Sample Input:

1 2 3 4 5 6 7 8 9

Sample Output:

[[1 2 3]
 [4 5 6]
 [7 8 9]]
 
'''


import numpy as np

def reshaping(arr):
    array = np.array(arr)
    reshaping = array.reshape(3,3)
    return reshaping

array_ele = list(map(int, input().split()))
array = np.array(array_ele)

result = reshaping(array)
print(result)


# Numpy Shape and Reshape