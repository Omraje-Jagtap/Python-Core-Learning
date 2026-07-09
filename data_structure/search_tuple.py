# search the number in the tuple.

tup = (11,2,3,4,5,5,6,7,8,9,0)         # this is linear type searching

a = int(input("enter the numberfor search:"))
count = 0 
index =0
for n in tup:
    
    if(n==a):
        count = count + 1
    
print(a,"found in this tuple",count,)