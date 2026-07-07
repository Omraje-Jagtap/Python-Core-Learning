'''Task:

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
solve using the function.

Input Format:
Read year,the year to test.

Constraints:
1990 <= yaer <= 10^5

Output Format:
The function must return a Boolean value (True/False).

Sample Input:
1990

Sample Output:
False'''

def is_leap(year):
    
    if 1990 <= year <= 10**5:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            return False
    else:
        print("Year must be between 1990 and 100000")
  
year = int(input())
print(is_leap(year))