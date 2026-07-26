'''Task:

You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format:
A single line containing a string .

Constraints:
0 < len(s) < 1000

Output Format:

In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
In the second line, print True if S has any alphabetical characters. Otherwise, print False.
In the third line, print True if S has any digits. Otherwise, print False.
In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.

Sample Input:
qA2

Sample Output:
True
True
True
True
True'''

if __name__ == '__main__':
    s = input()

alnum = False
alpha = False
digit = False
upper = False
lower = False

if len(s) > 0 and len(s) < 1000:
  for i in s:
    if i.isalnum() :
        alnum = True

    if i.isalpha():
        alpha = True
    
    if i.isdigit():
        digit =True
    
    if i.isupper():
        upper = True
    
    if i.islower():
        lower = True

print(("{}\n{}\n{}\n{}\n{}").format(alnum,alpha,digit,lower,upper))