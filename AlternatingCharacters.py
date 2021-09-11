#!/usr/bin/env python
# coding: utf-8

"""
You are given a string containing characters  A and B only. Your task is to change it 
into a string such that there are no matching adjacent characters. To do this, you are 
allowed to delete zero or more characters in the string. Your task is to find the minimum 
number of required deletions.

Function Description
Complete the alternatingCharacters function below.
alternatingCharacters has the following parameter(s):
INPUT:
    string s: a string
OUTPUT:
    int: the minimum number of deletions required

Link to problem statement:
https://www.hackerrank.com/challenges/alternating-characters/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'alternatingCharacters' function below.
The function is expected to return an INTEGER.
The function accepts STRING s as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/alternating-characters/problem
"""

def alternatingCharacters(s):
    # initialize the number of deletions
    deletions = 0
    # loop over the index of string s
    index = 0
    while index < len(s)-1:
        # find the adjacent index
        next_index = index + 1
        # check if the adjacent character is the same as current current
        if s[index] == s[next_index]:
            # update the deletions 
            deletions += 1
        # update character
        index = next_index
    return deletions 
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()
