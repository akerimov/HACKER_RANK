#!/usr/bin/env python
# coding: utf-8

"""
The previous challenges covered Insertion Sort, which is a simple and intuitive sorting algorithm 
with a running time of . In these next few challenges, we're covering a divide-and-conquer algorithm 
called Quicksort (also known as Partition Sort). This challenge is a modified version of the algorithm 
that only addresses partitioning. It is implemented as follows:
Choose some pivot element, p, and partition your unsorted array, arr, into three smaller arrays: 
left, right, and equal, where each element in left<p, each element in right>p, and each element in equal=p.

Function Description:
Complete the quickSort function below.
quickSort has the following parameter:
INPUT:
    int arr[n]:  is the pivot element
OUTPUT:
    int[n]: an array of integers as described above
    
Link to problem statement:
https://www.hackerrank.com/challenges/quicksort1/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'quickSort' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts INTEGER_ARRAY arr as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/quicksort1/problem
"""

def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    equal = []
    for num in arr:
        if num < p:
            left.append(num)
        elif num > p: 
            right.append(num)
        else:
            equal.append(num)
    return left + equal + right 

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    arr = list(map(int, input().rstrip().split()))
#    result = quickSort(arr)
#    fptr.write(' '.join(map(str, result)))
#    fptr.write('\n')
#    fptr.close()
