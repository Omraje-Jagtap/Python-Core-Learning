'''Task:
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Input Format:
The first line contains the integer n, the number of students' records. The next n lines
 contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
 
Constraints:
2 <= n <= 10
0 <= marks[i] < = 100
length of marks array =3'''



if __name__ == '__main__':
    n = int(input())
    if not (2 <= n <= 10):
        print("Number of students must be between 2 and 10")
    else:
        student_marks = {}
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            
            if len(scores) == 3 and all(0 <= s <= 100 for s in scores):
                student_marks[name] = scores
            else:
                print(f"Invalid input for {name}. Must have 3 marks between 0 and 100.")
        
        query_name = input()
        
        if query_name in student_marks.keys():
            marks = student_marks[query_name]
            average = sum(marks) / len(marks)
            print(f"{average:.2f}") 
        else:
            print("This name not available")


