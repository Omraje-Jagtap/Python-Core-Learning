'''Task:
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.

Average = (sum of total score obtained by student inalll subject) / (total number of subject)

The format for the general mark sheet is:

Student ID → ___1_____2_____3_____4_____5__               
Subject 1   |  89    90    78    93    80
Subject 2   |  90    91    85    88    86  
Subject 3   |  91    92    83    89    90.5
            |______________________________
Average        90    91    82    90    85.5

Input Format:
The first line contains N and X separated by a space.
The next N lines contains the space separated marks obtained by students in a particular subject.

Output Format:
Print the averages of all students on separate lines.
The averages must be correct up to 1 decimal place

Sample Input:

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Sample Output:

90.0 
91.0 
82.0 
90.0 
85.5 

'''

n,x = map(int, input().split())
if (n > 0 and n <= 100) and (x > 0 and x <= 100):

    marks_list = []
    for i in range(x):
        marks = list(map(float,input().split()))
        marks_list.append(marks)

    for i in range(len(marks_list[0])):
        colums = []
        for j in range(len(marks_list)):
            a = marks_list[j][i]
            colums.append(a)

        print(sum(colums)/len(colums))
        

# the another code using the numpy
'''import numpy as np

n,x = map(int, input().split())

marks_list = []
for i in range(x):
    marks = (input().split())
    array = np.array(marks,dtype=int)
    marks_list.append(array)

for i in marks_list:
    avg = sum(i)/ len(i)
    print(avg)'''