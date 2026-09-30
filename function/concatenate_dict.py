# WAF to concatenate any no dict to create a new one.

def concatenate(*dict):
    d = {}
    for i in dict:
        d.update(i)

    return d

d1 = {1:10,2:20}
d2 = {3:30,4:40}
d3 = {5:50,6:60}

merge = concatenate(d1,d2,d3)
print(merge)
