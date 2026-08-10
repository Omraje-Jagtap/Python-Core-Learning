'''Task:
You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
 
Constraints:
1 <= n <= 10^5
The sum of the lengths of all the words do not exceed 10^6
All the words are composed of lowercase English letters only

Input Format:
The first line contains the integer, n.
The next n lines each contain a word.

Output Format:
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input

Sample Input:
4
bcdef
abcdefg
bcde
bcdef

Sample Output:
3
2 1 1

'''
def count(str):
    count_str = []
    seen_words = []

    for i in str:
        if i not in seen_words:
            a = str.count(i)
            count_str.append(a)
            seen_words.append(i)

    return count_str

num = int(input())
if num <= 10 ** 5 and num >= 1:
    string = []
    for i in range(num):
        s = input()
        string.append(s)

    result = count(string)

    print(len(result))
    output = " ".join(map(str, result))
    print(output)
