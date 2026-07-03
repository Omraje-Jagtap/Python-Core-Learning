'''WAP to print grade of student based on marks 
    marks>=90,grade = a
    marks>=80,grade = b
    marks>=70,grade = c
    marks>=35,grade = d
    marks<35, fail'''
    


a = int(input("enter the marks:"))

if(a>=90):
    print("grade = A")

elif(a>=80):
    print("grade = B")
elif(a>=70):
    print("grade = C")
elif(a>=35):
    print("grade =  D")
else:
    print("fail")