#!/usr/bin/env python
# coding: utf-8

"""
You are given two arrays, A and B, both containing  integers. A pair of indices (i,j) is 
beautiful if the  element of array A is equal to the jth element of array B. In other words, 
(i,j) pair  is beautiful if and only if  A[i]=B[j]. A set containing beautiful pairs is 
called a beautiful set. A beautiful set is called pairwise disjoint if for every pair (l[i], r[i])
belonging to the set there is no repetition of either l[i] or r[i] values. Your task is to change 
exactly 1  element in B so that the size of the pairwise disjoint beautiful set is maximum.

Function Description:
Complete the beautifulPairs function below. It should return an integer that represents 
the maximum number of pairwise disjoint beautiful pairs that can be formed.

beautifulPairs has the following parameters:
INPUT: 
    A: an array of integers
    B: an array of integers
OUTPUT:
    Determine and print the maximum possible number of pairwise disjoint beautiful pairs.

Link to problem statement:
https://www.hackerrank.com/challenges/beautiful-pairs/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'beautifulPairs' function below.
The function is expected to return an INTEGER.
The function accepts following parameters:
  1. INTEGER_ARRAY A
  2. INTEGER_ARRAY B

Link to problem statement:
https://www.hackerrank.com/challenges/beautiful-pairs/problem
"""

def beautifulPairs(A, B):
    # initialize the beautiful pairs count
    beautiful_pairs= 0
    # loop over each element in A
    for num_A in A:
        # check if current element exist in B
        if num_A in B:
            # remove the current element from B
            B.remove(num_A)
            # update the beautiful pairs counts
            beautiful_pairs += 1
            
    # check if beautiful pairs counts is equal to length of A
    if beautiful_pairs == len(A):
        # substract exactly 1 pair and return 
        return beautiful_pairs -1
    # if beautiful pairs counts is less than len(A) add exactly 1 pair 
    return beautiful_pairs + 1 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    result = beautifulPairs(A, B)
    fptr.write(str(result) + '\n')
    fptr.close()
