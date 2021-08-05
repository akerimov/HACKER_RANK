#!/usr/bin/env python
# coding: utf-8

"""
Watson gives Sherlock an array of integers. His challenge is to find an element of the array 
such that the sum of all elements to the left is equal to the sum of all elements to the right.

Function Description:
Complete the balancedSums function below.
balancedSums has the following parameter(s):
INPUT:
    int arr[n]: an array of integers
OUTPUT:
    string: either YES or NO
    
Link to problem statement: 
https://www.hackerrank.com/challenges/sherlock-and-array/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'balancedSums' function below.
The function is expected to return a STRING.
The function accepts INTEGER_ARRAY arr as parameter.

Link to problem statement: 
https://www.hackerrank.com/challenges/sherlock-and-array/problem
"""

def balancedSums(arr):
    # since left and right sum to zero  
    if len(arr) == 1:
        return "YES"

    # start from index 0, then left sums up to 0, 
    # right sums up to sum of array minus first item    
    index = 0
    left_sum = 0
    right_sum = sum(arr[index+1:])
    
    # loop over each element in the array      
    while index < len(arr)-1: 
       # check if sum of all elements to the left 
       # is equal to the sum of all elements to the right 
        if left_sum == right_sum:
            return "YES"
        # update the sum of all elements to the left 
        left_sum += arr[index]
        # update the sum of all elements to the right  
        right_sum -= arr[index+1] 
        #update index
        index +=1
    return "NO"
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = balancedSums(arr)
        fptr.write(result + '\n')
    fptr.close()
