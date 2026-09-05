'''Task:
You have to generate a list of the first N fibonacci numbers, 0 being the first number.
Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

Input Format:

One line of input: an integer N.

Constraints:

0 <= N <= 15

Output Format:

A list on a single line containing the cubes of the first N fibonacci numbers.

Sample Input:

5

Sample Output:

[0, 1, 1, 8, 27]

Explanation:

The first 5 fibonacci numbers are [0,1,1,2,3], and their cubes are [0,1,1,8,27].

'''

cube = lambda x: x ** 3

def fibonacci(n):
    if 0 <= n <= 15:
        if n == 0:
            return []
        elif n == 1:
            return [0]
        else:
            fibo = [0,1]
            a = 0
            b = 1
            c = 0
            for i in range(n-2):
                c = a + b
                fibo.append(c)
                a = b
                b = c

            return fibo
        

    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))