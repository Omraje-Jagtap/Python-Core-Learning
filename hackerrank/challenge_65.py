'''Task:

 - Perform append, pop, popleft and appendleft 
   methods on an empty deque d.

Input Format:

 - The first line contains an integer N, the number of operations.
 - The next N lines contains the space separated names of methods 
   and their values.

Constraints:

 - 0 < N < 100

Output Format:

Print the space separated elements of deque d.

Sample Input:

6
append 1
append 2
append 3
appendleft 4
pop
popleft

Sample Output:

1 2

'''


from collections import deque

queue = deque()

def perform_queue_op(operation,q,n):

    if 0 < n < 100:

        for i in range(n):

            if operation[i][0] == 'append':
                q.append(operation[i][1])

            elif operation[i][0] == 'appendleft':
                q.appendleft(operation[i][1])

            elif operation[i][0] == 'pop':
                q.pop()

            elif operation[i][0] == 'popleft':
                q.popleft()


    return " ".join(q)


N = int(input())
operations = []

for i in range(N):
    op = list(map(str, input().split()))
    operations.append(op)


result = perform_queue_op(operations,queue,N)
print(result)

