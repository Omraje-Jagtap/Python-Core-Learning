'''You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:

1
22
333
4444
55555
......

 - Can you do it using only arithmetic operations, a single for loop and print statement?

 - Use no more than two lines.
   The first line (the for statement) is already written for you. You have to complete the print statement.

Note: 
Using anything related to strings will give a score of 0.

Input Format:
A single line containing integer, N.

Constraints:

1 <= N <= 9

Output Format:
Print N-1 lines as explained above.

Sample Input:

5

Sample Output:

1
22
333
4444

'''

N = int(input())
for i in range(1, N if 1 <= N <= 9 else 1): print(((10**i - 1)//9) * i)



# the another Solution of this challenge by manuallly not using the two lines of code.

'''N = int(input())
a = "0"
if 0 <= N <= 9:
    for i in range(1,N):
        a = a +"1"
        print((int(a[1:]))*i)

'''