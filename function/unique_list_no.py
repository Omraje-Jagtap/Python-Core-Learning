#WAF that takes a list and return a new list with unique element of first list

def unique(list):
    unique_set = set()
    for n in list:
        unique_set.add(n)
        
    
    new_list = []
    for i in unique_set:
        new_list.append(i)
    return new_list

list = []

user_no = input("enter the numbers with spaces:")
spliting = user_no.split(" ")

for str in spliting:
    num = int(str)
    list.append(num)

unique_new_list = unique(list)
print(unique_new_list)


        
    