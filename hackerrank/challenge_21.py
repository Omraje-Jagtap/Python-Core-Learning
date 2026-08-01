'''Task:
There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B.
Your initial happiness is 0. For each i integer in the array, if i intersect A, you add 1 to your happiness. If i interect B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Constraints:
1<= n <= 10^5
1<= m <= 10^5
1<= any integer in the input <= 10^9

Input Format:

The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
The third and fourth lines contain m integers, A and B, respectively.

Output Format:
Output a single integer, your total happiness.

Sample Input:
3 2
1 5 3
3 1
5 7
Sample Output:
1

'''

def happiness_score(array, set1, set2):
    happiness = 0
    for i in array:
        if i in set1:
            happiness += 1
        elif i in set2:
            happiness -= 1
    return happiness

n, m = map(int, input().split())
array = list(map(int, input().split()))
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

result = happiness_score(array, set1, set2)
print(result)