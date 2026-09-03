'''Task:
You are given a string N.
Your task is to verify that N is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

> Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5

> Number must contain at least 1 decimal value.
For example:
✖
 12.
✔
12.0  

> Number must have exactly one . symbol.
> Number must not give any exceptions when converted using flaot(N).

Input Format:

The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.

Constraints:

 - 0 < T < 10

Output Format:

Output True or False for each test case.

Sample Input:

4
4.0O0
-1.00
+4.54
SomeRandomStuff

Sample Output:

False
True
True
False

Explanation:

4.0O0 : O is not a digit.
-1.00 : is valid.
+4.54 : is valid.
SomeRandomStuff: is not a number'''



T = int(input().strip())

for _ in range(T):
    s = input().strip()
    try: 
        if 0 < T < 10:
            if s.count('.') != 1:
                print(False)
                continue

            float(s)

            dot_index = s.index('.')
            if dot_index == len(s) - 1:
                print(False)
            elif not any(ch.isdigit() for ch in s[dot_index+1:]):
                print(False)
            else:
                print(True)
    except:
        print(False)
