'''Task:
 
 - You are given an expression in a line. Read that line as a string variable, 
   such as var, and print the result using eval(var).

Input format:

 - the first line contains expression in string format

Constraint:

 - Input string is less than 100 characters.
 
Output format:

 - print the output of the expression after evaluation
 
Sample Input:

print(2 + 3)

Sample Output:

5

'''


def evaluation(exp):

    if len(exp) < 100:

        expression = exp.find('(')
        e = exp[expression:]
        evaluton = eval(e)

        return evaluton



expression = input()

result = evaluation(expression)
print(result)