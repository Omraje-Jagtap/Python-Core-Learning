'''TASK:

 - You are given a set A and N number of other sets. These N number of sets have to perform some 
   specific mutation operations on set A.

 - Your task is to execute those operations and print the sum 
   of elements from set A.

Input Format:

 - The first line contains the number of elements in set A.
 - The second line contains the space separated list of elements in set A.
 - The third line contains integer N, the number of other sets.
 - The next 2 * N lines are divided into N parts containing two lines each.
 - The first line of each part contains the space separated entries of the 
   operation name and the length of the other set.
 - The second line of each part contains space separated list of elements in the other set.

Constraints:

 - 0 < len(set(A)) < 1000
 - 0 < N < 100
 - 0 < len(otherSets) < 100


Output Format:

 - Output the sum of elements in set A.

Sample Input:

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66

Sample Output:

38

Explanation:

After the first operation, (intersection_update operation), we get:
set A = set([1,2,3,4,5,6,7,8,9,11])

After the second operation, (update operation), we get:
set set A = set([1,2,3,4,5,6,7,8,9,11,55,66])

After the third operation, (symmetric_difference_update operation), we get:
set A = set([1,2,3,4,5,6,7,8,9,11,22,35,55,58,62,66])

After the fourth operation, ( difference_update operation), we get:
set A = set([1,2,3,4,5,6,8,9])

The sum of elements in set A after these operations is 38


'''


def perfrom_set_operation(main_set,othersets,n):

    if (0 < len(main_set) < 1000)  and (0 < n < 100) and (0 < len(other_sets) < 100):

        for i in range(n):
            operations = othersets[i][0][0]

            if operations == "update":
                main_set.update(other_sets[i][1])
            elif operations == "intersection_update":
                main_set.intersection_update(other_sets[i][1])
            elif operations == "symmetric_difference_update":
                main_set.symmetric_difference_update(other_sets[i][1])
            elif operations == "difference_update":
                main_set.difference_update(other_sets[i][1])

        return sum(main_set)



A = int(input())
set_A = set(map(int, input().split()))
N = int(input())

other_sets = []

for i in range(N):
    operation = input().split()
    set_ele = set(map(int, input().split()))
    other_sets.append([operation,set_ele])

result = perfrom_set_operation(set_A,other_sets,N)
print(result)
