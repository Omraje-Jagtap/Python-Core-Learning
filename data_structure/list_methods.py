# WAP to check if a list contains a palindrome of elements.

a = input("enter the first elemnets of list:")
b = input("enter the second elemenets of list:")
c = input("enter third elementes of list:")

list = [a,b,c]

copy = list.copy()

list.reverse()
print(copy,list)

if(copy == list): print("the list is palindrome")
else: print("not palindrome")


