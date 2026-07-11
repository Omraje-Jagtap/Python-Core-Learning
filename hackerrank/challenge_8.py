'''Task: 
   You are given n scores. Store them in a list and find the score of the runner-up.

Input Format:
The first line contains n. The second line contains an array A[]  of n integers each separated by a space.

Constraints:
2 <= n <=10
-100 <= A[i] <= 100

Output Format:
Print the runner-up score.'''


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split())) 


if all(-100 <= x <= 100 for x in arr):
    
    max_score = max(arr)
    while max_score in arr:
        arr.remove(max_score)
    runner_up = max(arr)
    
    print(runner_up)

