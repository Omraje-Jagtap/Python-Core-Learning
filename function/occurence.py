# finding the large occurence.
def occurence(str):
    splitting = str.split(" ")
    new_count = 0
    for i in range(len(splitting)):
        count = 1
        for n in range(i+1,len(splitting)):
            if splitting[i] == splitting[n]:
                count = count + 1
        
        if new_count<count:
            new_count = count
    return new_count

# example input
a = occurence("hi hi hi am om om raje")
print(a)