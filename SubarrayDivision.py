#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Two children, Lily and Ron, want to share a chocolate bar. 
Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the bar selected such that:
    (1) The length of the segment matches Ron's birth month, and,
    (2) The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

Function Description
Complete the birthday function below.
birthday has the following parameter(s):
INPUT: 
    int s[n]: the numbers on each of the squares of chocolate
    int d: Ron's birth day
    int m: Ron's birth month
RETURN: %
    int: the number of ways the bar can be divided

Link to problem statement:
https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'birthday' function below.
The function is expected to return an INTEGER.
The function accepts following parameters:
  1. INTEGER_ARRAY s
  2. INTEGER d
  3. INTEGER m

Link to problem statement:
https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
"""

def birthday(s, d, m):
    segments_count = 0
    for index in range(len(s)-m+1):
        segment = s[index:index+m]
        print(segment)
        if sum(segment) == d:
            segments_count += 1
    return segments_count
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = birthday(s, d, m)
    fptr.write(str(result) + '\n')
    fptr.close()

