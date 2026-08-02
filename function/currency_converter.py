# WAF to convert the USD to INR.

def currency(USD):
    INR = USD*96
    return INR

US = int(input("enter the USD value to convert in INR:"))

IN = currency(US) #pasing USD as a argument
print("the value",US,"USD in INR is:",IN)

