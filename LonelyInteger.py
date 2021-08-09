#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Given an array of integers, where all elements but one occur twice, find the unique element.

Function Description:
Complete the lonelyinteger function in the editor below.

lonelyinteger has the following parameter(s):
INPUT:
    int a[n]: an array of integers
OUTPUT:
    int: the element that occurs only once

Link to problem statement:
https://www.hackerrank.com/challenges/largest-permutation/problem
"""


# In[ ]:


#!/bin/python3
import math
import os
import random
import re
import sys
from collections import Counter

"""
Complete the 'lonelyinteger' function below.
The function is expected to return an INTEGER.
The function accepts INTEGER_ARRAY a as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/lonely-integer/problem
"""

def lonelyinteger(a):
    # create dictionary: key=number, value=count
    num_count_dict = Counter(a)
    # reverse the dictionary: key=count, value=number
    count_num_dict = {value: key for key,value in num_count_dict.items()}
    # return number with count=1
    return count_num_dict[1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a)
    fptr.write(str(result) + '\n')
    fptr.close()

