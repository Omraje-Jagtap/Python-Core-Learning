'''Task:
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

Function Description:
Complete the swap_case function in the editor below.

swap_case has the following parameters:
string s: the string to modify
Returns
string: the modified string

Input Format:
A single line containing a string .

Constraints:
0 >= len(s) >= 1000'''

import string as str

def swap_case(s):
    if len(s) > 0 and len(s) < 1000:
        result = ""
        for i in s:
            if i in str.ascii_uppercase:
                result = result + i.lower()
            elif i in str.ascii_lowercase:
                result = result + i.upper()
            else:
                result = result + i
        return result
    else:
        print("enter the string lenght between 0 to 1000")


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)