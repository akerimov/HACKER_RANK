#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Given an array of stick lengths, use  of them to construct a non-degenerate triangle with the maximum possible perimeter. 
Return an array of the lengths of its sides as  integers in non-decreasing order. If there are several valid triangles 
having the maximum perimeter:
 (1) Choose the one with the longest maximum side.
 (2) If more than one has that maximum, choose from them the one with the longest minimum side.
 (3) If more than one has that maximum as well, print any one them.
 (4) If no non-degenerate triangle exists, return -1.

Function Description:
Complete the maximumPerimeterTriangle function below.
maximumPerimeterTriangle has the following parameter:
INPUT:
    int sticks[n]: the lengths of sticks available
OUTPUT:
    int[3] or int[1]: the side lengths of the chosen triangle in non-decreasing order or -1

Link to problem statement:
https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
"""


# In[ ]:


#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'maximumPerimeterTriangle' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts INTEGER_ARRAY sticks as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem
"""

def maximumPerimeterTriangle(sticks):
    #  sort the sticks in descending order
    sticks.sort(reverse=True)
    # loop over the stick lengths  
    for i in range(len(sticks)-2):
        # check if three sticks construct a non-degenerate triangle
        if ((sticks[i] + sticks[i+1])>sticks[i+2]) and ((sticks[i] + sticks[i+2])>sticks[i+1]) and ((sticks[i+2] + sticks[i+1])>sticks[i]):
            # return the side lengths of the chosen triangle in non-decreasing order 
            return(sorted([sticks[i], sticks[i+1], sticks[i+2]]))       
    # If no non-degenerate triangle exists, return -1
    return [-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    sticks = list(map(int, input().rstrip().split()))
    result = maximumPerimeterTriangle(sticks)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

