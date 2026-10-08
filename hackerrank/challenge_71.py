'''Task:

 - Now, let's use our knowledge of sets and help Mickey.
 - Ms. Gabriel Williams is a botany professor at District College. 
   One day, she asked her student Mickey to compute the average of all the 
   plants with distinct heights in her greenhouse.

 - Formula used:
     average = sum of the distinct heights / total number of the distinct heights

Function Description:

 - Complete the average function in the editor below.
 - average has the following parameters:

 - int arr: an array of integers

 Returns:

 - float: the resulting float value rounded to 3 places after the decimal

Input Format:

 - The first line contains the integer, N, the size of arr.
 - The second line contains the N space-separated integers, arr[i].

Constraints:

 - 0 < <= 100

Sample Input:

STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]

Sample Output:

169.375

'''


def average(array):
    distinct_heights = set(array)
    return round(sum(distinct_heights) / len(distinct_heights), 3)


if __name__ == '__main__':
    n = int(input())
    if not (0 < n <= 100):
        exit()
    arr = list(map(int, input().split()))
    result = average(arr)
    print(f"{result:.3f}")
