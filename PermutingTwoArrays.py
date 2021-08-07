#!/usr/bin/env python
# coding: utf-8

"""
There are two -element arrays of integers, A and B. Permute them into some A' and B' 
such that the relation A'[i] + B'[i] >= k holds for all i where 0<=i<n .

There will be q queries consisting of A, B, and k. For each query, return YES 
if some permutation A', B' satisfying the relation exists. Otherwise, return NO.

Function Description:
Complete the twoArrays function below. It should return a string, either YES or NO.
twoArrays has the following parameter:
INPUT:
    int k: an integer
    int A[n]: an array of integers
    int B[n]: an array of integers
OUTPUT:
    string: either YES or NO
    
Link to problem statement:
https://www.hackerrank.com/challenges/two-arrays/problem 
"""


#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'twoArrays' function below.
The function is expected to return a STRING.
The function accepts following parameters:
  1. INTEGER k
  2. INTEGER_ARRAY A
  3. INTEGER_ARRAY B

Link to problem statement:
https://www.hackerrank.com/challenges/two-arrays/problem  
"""

def twoArrays(k, A, B):
    # sort A array in descending order
    A.sort(reverse=True)
    # sort B array in ascending order
    B.sort(reverse=False)
   
    # loop over each index in A array
    for i in range(len(A)):
        # check the relation between permutation
        if A[i] + B[i] < k:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        A = list(map(int, input().rstrip().split()))
        B = list(map(int, input().rstrip().split()))
        result = twoArrays(k, A, B)
        fptr.write(result + '\n')
    fptr.close()
