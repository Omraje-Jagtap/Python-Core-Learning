'''Task:

 - You are given a space separated list of numbers.
 - Your task is to print a reversed NumPy array with the element type float.

Input Format:

 - A single line of input containing space separated numbers.

Output Format:

 - Print the reverse NumPy array with type float.

Sample Input:

1 2 3 4 -8 -10

Sample Output:

[-10.  -8.   4.   3.   2.   1.]

'''


import numpy as np

def arrays(arr):
    positive = []
    negative = []
    array = np.array(arr, float)

    for i in array:
        if i < 0:
            negative.append(i)
        else:  
            positive.append(i)

    sorted_negative = np.sort(np.array(negative))

    sorted_positive = np.sort(np.array(positive))[::-1]

    arr = np.concatenate((sorted_negative, sorted_positive))
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
