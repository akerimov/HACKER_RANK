#!/usr/bin/env python
# coding: utf-8

"""
Consider an array of numeric strings where each string is a positive number with anywhere 
from  to  digits. Sort the array's elements in non-decreasing, or ascending order of their 
integer values and return the sorted array.

Function Description:
Complete the bigSorting function below.
bigSorting has the following parameter:
INPUT:
    string unsorted[n]: an unsorted array of integers as strings
OUTPUT:
    string[n]: the array sorted in numerical order
    
Link to problem statement:
https://www.hackerrank.com/challenges/big-sorting/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'bigSorting' function below.
The function is expected to return a STRING_ARRAY.
The function accepts STRING_ARRAY unsorted as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/big-sorting/problem
"""

def bigSorting(unsorted):
    # sort the list of strings in place by integer value
    sorted_arr = unsorted.sort(key=int) 
    return sorted_arr
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)
    result = bigSorting(unsorted)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
