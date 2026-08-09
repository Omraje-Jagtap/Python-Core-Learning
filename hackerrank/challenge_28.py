'''Task:
Dr. John Wesley has a spreadsheet containing a list of student's IDs,marks,calss and name.
Your task is to help Dr. Wesley calculate the average marks of the students.

average = (sum of all marks)/total student

Input Format

The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks,IDs,name and claas,under their respective column names.

Constraints:
0 < N <= 100

Output Format:
Print the average marks of the list corrected to 2 decimal places.

Sample Input:

TESTCASE 01:
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   

TESTCASE 02:
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5

Sample Output:

TESTCASE 01:
78.00
TESTCASE 02
81.00
'''

from collections import namedtuple

n = int(input())
columns = input().split()

Student = namedtuple('Student', columns)

students = []
if n < 100 and n > 0:
    for _ in range(n):
        data = input().split()
        s = Student(*data)
        students.append(s)

marks_index = columns.index("MARKS")

marks_list = [int(getattr(s, columns[marks_index])) for s in students]

average = sum(marks_list) / len(marks_list)


print(f"{average:.2f}")

