#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
You are choreographing a circus show with various animals. 
For one act, you are given two kangaroos on a number line ready 
to jump in the positive direction (i.e, toward positive infinity).

(1) The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
(2) The second kangaroo starts at location x2  and moves at a rate of v2  meters per jump.

You have to figure out a way to get both kangaroos at the same location 
at the same time as part of the show. If it is possible, return YES, 
otherwise return NO.

Function Description
Complete the function kangaroo below.
kangaroo has the following parameter(s):
INPUT:
    int x1, int v1: starting position and jump distance for kangaroo 1
    int x2, int v2: starting position and jump distance for kangaroo 2
OUTPUT:
    string: either YES or NO

Link to problem statement:
https://www.hackerrank.com/challenges/kangaroo/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'kangaroo' function below.
The function is expected to return a STRING.
The function accepts following parameters:
  1. INTEGER x1
  2. INTEGER v1
  3. INTEGER x2
  4. INTEGER v2

Link to problem statement:
https://www.hackerrank.com/challenges/kangaroo/problem
"""

def kangaroo(x1, v1, x2, v2):
    # Because the second kangaroo moves at a faster rate 
    # and is already ahead of the first kangaroo, 
    # the first kangaroo will never be able to catch up
    if x2>x1 and v2>=v1:
        return "NO"
    
    # find number of jumps get both kangaroos at the same location at the same time
    number_jumps = (x1-x2)/(v2-v1)
    # check if number of jumps is positive and integer
    if number_jumps > 0 and (number_jumps - int(number_jumps))==0:
        return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()

