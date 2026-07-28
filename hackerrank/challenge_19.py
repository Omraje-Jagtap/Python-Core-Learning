'''Task:
given a string s and an integer k, split s into n/k substrings of length k.
For each substring, remove duplicate characters while preserving the order 
of their first occurrence. Print each processed substring on a new line.

Function Description:
Complete the merge_the_tools function in the editor below.
merge_the_tools has the following parameters:

-string s: the string to analyze
-int k: the size of substrings to analyze

Input Format:
The first line contains a single string,s.
The second line contains an integer, k, the length of each substring.

Constraints:
1<= n >= 10^4, where n is the length of s
1 <= k <= n
It is guaranteed that n is a multiple of k.

Sample Input:

STDIN       Function
-----       --------
AABCAAADA   s = 'AABCAAADA'
3           k = 3

Sample Output:
AB
CA
AD'''


def merge_the_tools(string, k):
    if (len(string) >= 1 and len(string) <= (10 ** 4)) and (k <= len(string) and k >= 1) and (len(string) % k == 0):
        for i in range(0,len(string),k):
            substr = string[i:i+k]
            result = ""
            for ch in substr:
                if ch not in result:
                    result = result + ch
            print(result)
    

if __name__ == '__main__':
    string, k = input(), int(input())
    result = merge_the_tools(string, k)