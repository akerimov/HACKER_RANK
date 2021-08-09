#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Given two integers, l and r, find the maximal value of a xor b, where a and b satisfy the following condition:
l<=a<=b<=r

Function Description:
Complete the maximizingXor function below. It must return an integer representing the maximum value calculated.

maximizingXor has the following parameter(s):
INPUT:
    l: an integer, the lower bound, inclusive
    r: an integer, the upper bound, inclusive
OUTPUT:
    Return the maximal value of the xor operations for all permutations of the integers from  l to r, inclusive.  
    
Link to problem statement:
https://www.hackerrank.com/challenges/maximizing-xor/problem
"""


# In[ ]:


#!/bin/python3
import math
import os
import random
import re
import sys
import itertools


"""
Complete the 'maximizingXor' function below.
The function is expected to return an INTEGER.
The function accepts following parameters:
  1. INTEGER l
  2. INTEGER r

Link to problem statement: 
https://www.hackerrank.com/challenges/maximizing-xor/problem
"""

def maximizingXor(l, r):
    # initialize xors list
    xors = []
    # loop over each combination of two integers between l and r
    for item in itertools.combinations(range(l,r+1),2):
        # compute the xor value and add to the list
        xors.append(item[0]^item[1])
    # return the maximum xor value
    return max(xors)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input().strip())
    r = int(input().strip())
    result = maximizingXor(l, r)
    fptr.write(str(result) + '\n')
    fptr.close()

