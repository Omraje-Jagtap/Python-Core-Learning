# WAF that accepts the string and calculate the no. of uppercase and lowercase letters.

import string

def count(str):
    uppercase = 0
    lowercase = 0
    for i in str:
        if i in string.ascii_uppercase:
            uppercase = uppercase + 1
        
        elif i in string.ascii_lowercase:
            lowercase = lowercase + 1
        
        else:
            pass
    return uppercase,lowercase

str = input("enter the string:")
x,y = count(str)
print("uppercase:",x,"\nlowercase:",y)
