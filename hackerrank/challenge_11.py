'''Task:
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of 
commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Input Format:
The first line contains an integer,n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints:
The elements added to the list must be integers.

Output Format:
For each command of type print, print the list on a new line.

Sample Input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]'''

if __name__ == '__main__':
    user_inpit = []
    N = int(input())
    for _ in range(N):
        user = input().split()
        user_inpit.append(user)

list = []

for i in range(N):
    sublist = []
    j = user_inpit[i][1:]
    method_name = user_inpit[i][0].lower()
    for k in j:
        if method_name in ["insert", "append", "remove"]:
            convert = int(k)
            sublist.append(convert)
        else:
            sublist.append(k)
    list.append(sublist)

for x in range(N):
    method_name = user_inpit[x][0]
    list[x].insert(0, method_name)

new_list = []

for s in range(N):
    if list[s][0].lower() == "insert":
        new_list.insert(list[s][1], list[s][2])
    
    elif list[s][0].lower() == "print":
        print(new_list)

    elif list[s][0].lower() == "remove":
        new_list.remove(list[s][1])

    elif list[s][0].lower() == "append":
        new_list.append(list[s][1])

    elif list[s][0].lower() == "sort":
        new_list.sort()

    elif list[s][0].lower() == "pop":
        new_list.pop()
    
    elif list[s][0].lower() == "reverse":
        new_list.reverse()
