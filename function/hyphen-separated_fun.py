# WAF that accept q hypen-separated sequence od words as parameter and returns the words in hypen-separated squence after sorting.

def hypen_sort(str):
    temp = []
    spliting = str.split("-")
    for n in spliting:
        temp.append(n)
    temp.sort()
    return "-".join(temp)

user_input = input("enter the hypen separated words:")

a = hypen_sort(user_input)
print(a)