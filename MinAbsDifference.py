#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Given an array of integers, find the minimum absolute difference between any two elements in the array.

Function Description:
Complete the minimumAbsoluteDifference function below. It should return an integer that 
represents the minimum absolute difference between any pair of elements.

minimumAbsoluteDifference has the following parameter:
INPUT:
    int arr[n]: an array of integers
OUTPUT:
    int: the minimum absolute difference found
    
Link to problem statement:
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem 
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'minimumAbsoluteDifference' function below.
The function is expected to return an INTEGER.
The function accepts INTEGER_ARRAY arr as parameter.

Link to problem statement: 
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
"""

def minimumAbsoluteDifference(arr):
    arr.sort(reverse=False)
    diff_arr = []
    for index in range(len(arr)-1):
        diff_arr.append(abs(arr[index+1] - arr[index]))
    #print(diff_arr)
    return min(diff_arr)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

