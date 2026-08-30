'''Task:
ABC is a right triangle, 90 at B.
Therefore, angle ABC = 90.

Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC.
Your task is to find anagle MBC (angle theta degree, as shown in the figure) in degrees.

Input Format:

The first line contains the length of side AB.
The second line contains the length of side BC.

Constraints:
 - 0 < AB <= 100
 - 0 < BC <= 100
 - Lengths AB and BC are natural numbers.

Output Format:

Output angle MBC in degrees.

Note: Round the angle to the nearest integer.

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.
0 < theta < 90

Sample Input:

10
10

Sample Output:

45°

'''

import math

def angle_MBC(ab,bc):
    if 0 < ab <= 100 and 0 < bc <= 100:
        theta = math.acos((bc) / (math.sqrt((math.pow(ab,2)) + (math.pow(bc,2)))))
        degree = math.degrees(theta)
        round_up = round(degree)
        return "{}\u00B0".format(round_up)


AB = int(input())
BC = int(input())

result = angle_MBC(AB,BC)
print(result)