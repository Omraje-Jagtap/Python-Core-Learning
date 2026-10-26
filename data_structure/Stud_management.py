# Question: Write a Python program to store student marks
# in a dictionary and find the average marks.

def calculate_average(marks):
    total = sum(marks.values())
    return total / len(marks)


students = {
    "karan": 85,
    "Om": 75,
    "sarthak": 90,
    "vaishnavi": 80
}

for name, marks in students.items():
    print(name, ":", marks)

print("Average marks:", calculate_average(students))
