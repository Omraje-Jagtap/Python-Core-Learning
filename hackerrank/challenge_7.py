'''Task:
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.

Example:
n = 5
Print the string 12345.

Input Format:
The first line contains an integer n.

Constraints:
1 <= n < 150'''

if __name__ == '__main__':
    n = int(input())
    
def print_string(n):
    if n >= 1 and n <= 150:
        for i in range(1,n+1):
            string = i.__format__("")
            print(string,end="")
            
print_string(n)