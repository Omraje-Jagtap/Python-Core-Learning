# WAF to print the elements of list in a single line. 

def element(list): #takling list as  parameter
    for n in list:
        print(n, end=",")

ls = []

list_element = input("enter the element of list with space:")  # take input of element in list from user
a = list_element.split(" ")

for i in a:
    ls.append(i)  # add the every element in list

print(ls)
element(ls) #passing arguments to element function
