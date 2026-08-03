'''Task:
You are given a string S and width w.
Your task is to wrap the string into a paragraph of width w.

Function Description:
Complete the wrap function in the editor below.
wrap has the following parameters:
  - string string: a long string
  - int max_width: the width to wrap to
  
Returns:
string: a single string with newline characters ('\n') where the breaks should be

Input Format:
The first line contains a string, string.
The second line contains the width, max_width.

Constraints:
0 < len(string) < 1000
0 < max_width < len(string)

Sample Input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4

Sample Output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

'''
import textwrap
# using the textwrap module.
def wrap(string, max_width):
    if (len(string) > 0 and len(string) < 1000) and (max_width > 0 and max_width < len(string)):
        wrap = textwrap.fill(string,max_width)
        return wrap
        
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
print("-------------------------------------------------------------------------------------------------------------------------------")

# using the normal loops and list concept.
def wrap2(string, max_width):
    str = []
    for i in range(0,len(string),max_width):
        a = string[i:i+max_width]
        str.append(a)

    return str
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap2(string, max_width)

    for i in result:
        print(i)