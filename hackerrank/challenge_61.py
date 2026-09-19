'''Task:

 - You are given a text of N lines. The text contains && and || symbols.
 - Your task is to modify those symbols to the following:

&& → and
|| → or

 - Both && and || should have a space " " on both sides.

Input Format:

 - The first line contains the integer, N.
 - The next N lines each contain a line of the text.

Constraints:

 - 0 < N < 100
 - Neither && nor || occur in the start or end of each line.

Output Format:

 - Output the modified text.

Sample Input:

11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.

Sample Output:

a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.    


'''

def replace_txt(n):
    if 0 <  n < 100:
        data = []
        for i in range(n):
            liines = input()
        
            while True:
                old_line = liines
            
                if " && " in liines and " &&& " not in liines:
                    liines = liines.replace(" && ", " and ")
                
                if " || " in liines and " ||| " not in liines:
                    liines = liines.replace(" || ", " or ")
                
                if liines == old_line:
                    break
                
            data.append(liines)

        join__data = "\n".join(data)
        return join__data

N = int(input())
result = replace_txt(N)
print(result)


# another way to finding the same result.

'''import re

# def replace_txt(n):
#     data = []
#     for i in range(n):
#         liines = input()
        
#         # (?<= ) means "preceded by a space"
#         # (?= ) means "followed by a space"
#         liines = re.sub(r'(?<= )&&(?= )', 'and', liines)
#         liines = re.sub(r'(?<= )\|\|(?= )', 'or', liines)
        
#         data.append(liines)

#     join__data = "\n".join(data)
#     return join__data

# N = int(input())
# result = replace_txt(N)
# print(result)


'''