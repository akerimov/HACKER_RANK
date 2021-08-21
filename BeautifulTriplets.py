#!/usr/bin/env python
# coding: utf-8

"""
Given a sequence of inetegrs arr, a triplet (arr[i], arr[j], arr[k]) is beautiful if:
    (1) i<j<k
    (2) a[j] - a[i] = a[k] - a[j] = d
    
Given an increasing sequence of integers and the value of d,count the number of 
beautiful triplets in the sequence.

Function Description
Complete the beautifulTriplets function below.
beautifulTriplets has the following parameters:
INPUT:
    int d: the value to match
    int arr[n]: the sequence, sorted ascending
OUTPUT:
    int: the number of beautiful triplets

Link to problem statement: 
https://www.hackerrank.com/challenges/beautiful-triplets/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'beautifulTriplets' function below.
The function is expected to return an INTEGER.
The function accepts following parameters:
  1. INTEGER d
  2. INTEGER_ARRAY arr

Link to problem statement: 
https://www.hackerrank.com/challenges/beautiful-triplets/problem
"""

def beautifulTriplets(d, arr):
    # iniialize count of beautiful triples
    beautiful_triplets = 0 
    
    # loop over the index of the array
    for index in range(len(arr)):
        # find the sequence of integers to satisfy beautiful triplet
        ai = arr[index]
        aj = ai + d
        ak = ai + 2*d     
        # check if aj and ak exist in the remaining array 
        if aj in arr[index+1:] and ak in arr[index+1:]:
            # update the count of beautiful triples
            beautiful_triplets += 1

    return beautiful_triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
