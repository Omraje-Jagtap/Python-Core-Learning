'''Task:
 - You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, 
   in order of their occurrence from top to bottom.

CSS Code Pattern:

Selector
{
	Property: Value;
}


Input Format:

 - The first line contains N, the number of code lines.
 - The next N lines contains CSS Codes.

Constraints:

 - 0 < N < 50

Output Format:

 - Output the color codes with '#' symbols on separate lines.

Sample Input:

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}  

Sample Output:

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

Explanation:

#BED and #Cab satisfy the Hex Color Code criteria, 
but they are used as selectors and not as color codes in the given CSS.

Hence, the valid color codes are:

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

Note: 
 - There are no comments ( // or /* */) in CSS Code.

'''


import re

N = int(input())

inside_block = False

for _ in range(N):
    line = input()

    if "{" in line:
        inside_block = True
        continue

    if "}" in line:
        inside_block = False
        continue

    if inside_block:
        colors = re.findall(r'#[0-9a-fA-F]{3}(?![0-9a-fA-F])|#[0-9a-fA-F]{6}(?![0-9a-fA-F])', line)

        for color in colors:
            print(color)



# another way to finding the same result.

'''N = int(input())

def color_code(code, N):
    if 0 < N < 50:
        color_codes = []
        inside_block = False

        for i in code:
            if i.strip() == "{":
                inside_block = True
            elif i.strip() == "}":
                inside_block = False
            elif inside_block and "#" in i:
                # assign the cleaned string
                cleaned = i.replace(";", " ").replace(":", " ").replace(",", " ").replace(")", " ").replace("(", " ")
                parts = cleaned.split()
                for part in parts:
                    if part.startswith('#'):
                        color_codes.append(part.strip(';:,)'))

        return color_codes
    return []


css_code = []
for i in range(N):
    lines = input()
    css_code.append(lines)

result = color_code(css_code, N)

for code in result:
    print(code)
    
'''
