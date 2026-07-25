'''Task:
the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

Input Format:
The first line of input contains the original string. The next line contains the substring. 

Constraints:
1>= len(string) <= 200
Each character in the string is an ascii character.

Output Format:
Output the integer number indicating the total number of occurrences of the substring in the original string.'''

def count_substring(string, sub_string):
    if len(string) >= 1 and len(string) <= 200:
        length = len(sub_string)
        count = 0

        for j in range(len(string)):
            a = string[j:j+length]
            if a == sub_string:
                count += 1    

        return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)