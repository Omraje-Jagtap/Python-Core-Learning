'''Task:
You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:

 - All sorted lowercase letters are ahead of uppercase letters.
 - All sorted uppercase letters are ahead of digits.
 - All sorted odd digits are ahead of sorted even digits.
 
Input Format:

A single line of input contains the string S.

Constraints:

 - 0 < len(s) < 1000

Output Format:

Output the sorted string S.

Sample Input:

Sorting1234

Sample Output:

ginortS1324

'''



def ginsort(string):
    lower = []
    upper = []
    number = ["1","2","3","4","5","6","7","8","9","0"]
    num = []

    if 0 < len(string) < 1000:
        for i in string:
            if i.islower():
                lower.append(i)
            elif i.isupper():
                upper.append(i)
            elif i in number:
                num.append(i)
            else:
                pass

        odds = []
        even = []

        for i in num:
            if int(i) % 2 == 0:
                even.append(i)
            elif int(i) % 2 != 0:
                odds.append(i)
            else:
                pass 

        sorted_string = "".join(sorted(lower)) + "".join(sorted(upper)) + "".join(sorted(odds)) + "".join(sorted(even))

        return sorted_string


S = input()

print(ginsort(S))