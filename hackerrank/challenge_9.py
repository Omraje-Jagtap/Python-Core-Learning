'''Task:
Given the names and grades for each student in a class of N students, store them in 
a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.

Constraints:
2 <= N <= 5
There will always be one or more students having the second lowest grade.'''


if __name__ == '__main__':
    N = int(input())

    if N < 2 or N > 5:
        print("Number of students must be between 2 and 5.")
    else:
        name_score = []
        for _ in range(N):
            name = input()
            score = float(input())
            name_score.append([name, score])

scores = []       
for i in range(len(name_score)):
    scores.append(name_score[i][1])

low_score = min(scores)

while low_score in scores:
    scores.remove(low_score)

second_lowest_score = min(scores)

name_second_low_score = []

for i in range(len(name_score)):
    if second_lowest_score == name_score[i][1]:
        name_second_low_score.append(name_score[i][0])

sorted_names = sorted(name_second_low_score)

for i in sorted_names:
    print(i)



