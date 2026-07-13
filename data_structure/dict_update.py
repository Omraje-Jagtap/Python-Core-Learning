# the accept marks of three student with their subjects and store it in dictonary.

dict = {}

sub1 = str(input("enter the name of subject:"))
marsk1 = int(input("enter the marks of subject"))
sub2 = str(input("enter the name of subject:"))
marsk2 = int(input("enter the marks of subject"))
sub3 = str(input("enter the name of subject:"))
marsk3 = int(input("enter the marks of subject"))

dict1 = {sub1 : marsk1}
dict2 = {sub2 : marsk2}
dict3 = {sub3 : marsk3}

dict.update(dict1)
dict.update(dict2)
dict.update(dict3)

print(dict)