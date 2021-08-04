#!/usr/bin/env python
# coding: utf-8

"""
Sorting is useful as the first step in many different tasks. The most common task 
is to make finding things easier, but there are other uses as well. In this case, 
it will make it easier to determine which pair or pairs of elements have the smallest 
absolute difference between them. Given a list of unsorted integers, arr, find the 
pair of elements that have the smallest absolute difference between them. If there 
are multiple pairs, find them all.

Function Description:
Complete the closestNumbers function below.
closestNumbers has the following parameter:
INPUT:
    int arr[n]: an array of integers
OUTPUT:
    int[]: an array of integers as described
    
Link to problem statement:
https://www.hackerrank.com/challenges/closest-numbers/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'closestNumbers' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts INTEGER_ARRAY arr as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/closest-numbers/problem
"""

def closestNumbers(arr):
    # sort the arr in ascending order
    arr.sort()
    
    # loop over the elements in sorted arr
    diff = []
    for index in range(len(arr)-1):
        # calculate the abs difference between pairs of elements
        diff.append(abs(arr[index]-arr[index+1]))
    
    result = []
    # find the minimum difference between pairs of elements
    min_diff = min(diff)
    # loop over each difference between elements 
    # determine which pair elements have the smallest absolute difference 
    for index, num in enumerate(diff):
        # select the smallest difference
        if num == min_diff:
            # add the pair of elements with the smallest absolute difference
            result.extend([arr[index], arr[index+1]] )
    
    return result
        
    
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    arr = list(map(int, input().rstrip().split()))
#    result = findMedian(arr)
#    fptr.write(str(result) + '\n')
#    fptr.close()
