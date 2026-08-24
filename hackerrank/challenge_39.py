'''Task:
The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English newspaper,
one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Input Format:

The first line contains an integer,n, the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students

Constraints:
0 < Total Number Of Student in college < 1000

Output Format:
Output the total number of students who have subscriptions to both English and French newspapers.

Sample Input:

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output:

5

'''


def print_intersection(set1,set2):
    intersection_set = set1.intersection(set2)
    if 0 < len(intersection_set) < 1000:
        return intersection_set


n1 = int(input())
b1 = set(map(int, input().split()))
n2 = int(input())
b2 = set(map(int, input().split()))

intersection_set = print_intersection(b1,b2)
result = len(intersection_set)
print(result)