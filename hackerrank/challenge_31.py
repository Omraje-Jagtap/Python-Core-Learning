'''Task:
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
They are now trying out various combinations of company names and logos based on this condition.
Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

 - Print the three most common characters along with their occurrence count.
 - Sort in descending order of occurrence count.
 - If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above,
GOOGLE would have it's logo with the letters G,O,E.

Input Format:
A single line of input containing the string S.

Constraints:
 - 3 < len(s) <= 10^4
 - S has at least 3 distinct characters
 
Output Format:
 - Print the three most common characters along with their occurrence count each on a separate line.
 - Sort output in descending order of occurrence count.
 - If the occurrence count is the same, sort the characters in alphabetical order
 
Sample Input:
aabbbccde

Sample Output:
b 3
a 2
c 2

'''

def company_logo(s):
    if len(s) > 3 and len(s) <= 10 **4:
        list_ = []
        for i in s:
            list_.append(i)

        dictionary = {}
        for j in list_:
            count = list_.count(j)
            dictionary[j] = count

        d = dict(sorted(dictionary.items(),key=lambda x: (x[1], x[0])))
        top3 = list(d.items())[:3]
        return top3
        

if __name__ == '__main__':
    s = input()

    result = company_logo(s)

    for i,j in result:
        print(i,j)