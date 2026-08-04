'''Task:
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
Given a full name, your task is to capitalize the name appropriately.

Input Format:
A single line of input containing the full name,S.

Constraints:
 -0 < len(s) < 1000
 -The string consists of alphanumeric characters and spaces.
 
 Output Format:
Print the capitalized string,S.

Sample Input:
chris alan

Sample Output:
Chris Alan

'''
import math
import os
import random
import re
import sys

def solve(s):
    words = []
    for i in s.split(" "):   
        if i:                
            words.append(i[0].upper() + i[1:])
        else:
            words.append("")
    return " ".join(words)

if __name__ == '__main__':
    s = input()

    result = solve(s)
    print(result)
