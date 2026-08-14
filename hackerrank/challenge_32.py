'''There is a horizontal row of n cubes. The length of each cube is given. You need to create a new vertical pile of cubes.
The new pile should follow these directions: if cube[i] is on top of cube[j] then sidelength[i] >= sidelength[j].
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time.
Print Yes if it is possible to stack the cubes. Otherwise, print No.

Example:
block = [1,2,3,8,7]
Result: No

After choosing the rightmost element,7, choose the leftmost element, 1. After than, the choices are 2 and 8.
These are both larger than the top block of size 1.

block = [1,2,3,7,8]
Result: Yes
Choose blocks from right to left in order to successfully stack the blocks

Input Format:

The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each cube in that order.

Constraints:
1 <=  T <= 5
a <= n <= 10^5
1 <= sidelength < 2^31

Output format:
For each test case, output a single line containing either Yes or No

Sample Input:

STDIN        Function
-----        --------
2            T = 2
6            blocks[] size n = 6
4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
3            blocks[] size n = 3
1 3 2        blocks = [1, 3, 2]

Sample Output:
Yes
No

'''

from collections import deque

def can_stack(cubes):
    cubes = deque(cubes)
    last = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            pick = cubes.popleft()
        else:
            pick = cubes.pop()

        if pick > last:
            return "No"
        last = pick

    return "Yes"

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    cubes = list(map(int, input().split()))
    print(can_stack(cubes))
