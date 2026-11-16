'''Question: write program for the postfix expression evaluation '''

stack = []

exp = "5 3 2 * +"

splitting = exp.split()

for i in splitting :

    if i.isdigit():
        stack.append(int(i))

    else:
        b = stack.pop()
        a = stack.pop()

        if i == '+':
            stack.append(a + b)

        elif i == '-':
            stack.append(a - b)

        elif i == '*':
            stack.append(a * b)

        elif i == '/':
            stack.append(a / b)

print("Result:", stack.pop())
