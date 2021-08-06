#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance 
to expend those calories. If Marc has eaten j cupcakes so far, after eating a cupcake with c calories he must walk 
at least 2jxc miles to maintain his weight.

Function Description:
Complete the marcsCakewalk function below.
marcsCakewalk has the following parameter:
INPUT:
    int calorie[n]: the calorie counts for each cupcake
OUTPUT:
    long: the minimum miles necessary
    
Link to problem statement:
https://www.hackerrank.com/challenges/marcs-cakewalk/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'marcsCakewalk' function below.
The function is expected to return a LONG_INTEGER.
The function accepts INTEGER_ARRAY calorie as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/marcs-cakewalk/problem
"""

def marcsCakewalk(calorie):
    # sort calorie list in descending order
    calorie.sort(reverse = True)
    # initialize the miles to maintain his weight
    min_miles = 0
    # loop over the each cupcake calorie
    for index in range(len(calorie)):
        # update the miles 
        min_miles += (2**index)*calorie[index]
    # return minimum miles required tomain tain his weight    
    return min_miles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    calorie = list(map(int, input().rstrip().split()))
    result = marcsCakewalk(calorie)
    fptr.write(str(result) + '\n')
    fptr.close()

