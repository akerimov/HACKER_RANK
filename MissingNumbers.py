#!/usr/bin/env python
# coding: utf-8

"""
Given two arrays of integers, find which elements in the second array are missing from the first array.
If a number occurs multiple times in the lists, you must ensure that the frequency of that number in both 
lists is the same. If that is not the case, then it is also a missing number. Return the missing numbers 
sorted ascending. Only include a missing number once, even if it is missing multiple times. The difference 
between the maximum and minimum numbers in the original list is less than or equal to 100.

Function Description:
Complete the missingNumbers function below. 
It should return a sorted array of missing numbers.
missingNumbers has the following parameters:
INPUT:
    int arr[n]: the array with missing numbers
    int brr[m]: the original array of numbers
OUTPUT:
    int[]: an array of integers
    
Link to problem statement: 
https://www.hackerrank.com/challenges/missing-numbers/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

"""
Complete the 'missingNumbers' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts following parameters:
  1. INTEGER_ARRAY arr
  2. INTEGER_ARRAY brr

Link to problem statement:
https://www.hackerrank.com/challenges/missing-numbers/problem
"""

def missingNumbers(arr, brr):
    # count dictionary of original array and array with missing
    arr_count = Counter(arr)
    brr_count = Counter(brr)
    
    # loop over the numbers in original array
    missing_numbers = []
    for key in brr_count:
        # check whether a number from original array is not in array with missing numbers
        # or frequency of that number in both arrays is not the same 
        if key not in arr_count.keys() or brr_count[key] != arr_count[key]:
            # add the missing number
            missing_numbers.append(key)
    
    # return array with elements in the second array are missing from the original array
    return sorted(missing_numbers)
 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
