'''Task:
You are given a date. Your task is to find what the day is on that date.

Input Format:
A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

Constraints:
2000 > year < 3000

Output Format:
Output the correct day in capital letters.

Sample Input:
08 05 2015

Sample Output"
WEDNESDAY'''


import calendar as cd
def day(list):
    if list[2] > 2000 and list[2] < 3000:
        a = cd.weekday(list[2],list[0],list[1])
        return cd.day_name[a].upper()

user_input  = list(map(int, input().split()))
day_ = day(user_input)
print(day_)
