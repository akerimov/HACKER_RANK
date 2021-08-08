#!/usr/bin/env python
# coding: utf-8

"""
You are given an unordered array of unique integers incrementing from . You can swap any two elements a limited number of times. 
Determine the largest lexicographical value array that can be created by executing no more than the limited number of swaps.

Function Description:
Complete the largestPermutation function below. 
It must return an array that represents the highest value permutation that can be formed.

largestPermutation has the following parameter(s):
INPUT:
    int k: the maximum number of swaps
    int arr[n]: an array of integers
OUTPUT: 
    Print the lexicographically largest permutation you can make with at most k swaps.

Link to problem statement:
https://www.hackerrank.com/challenges/largest-permutation/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'largestPermutation' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts following parameters:
  1. INTEGER k
  2. INTEGER_ARRAY arr

Link to problem statement:
https://www.hackerrank.com/challenges/largest-permutation/problem
"""

def largestPermutation(k, arr):
    # create dictionary: key=index, value=numbers
    index_num_dict = dict(enumerate(arr))
    # create dictionary: key=number, value=index
    num_index_dict = {num:index for index, num in index_num_dict.items()}
    # largest number in array incrementing from 1
    max_number = len(arr)
    
    # loop over each index in array and swap parameter
    i = 0
    while k >0 and i<len(arr):
        # check if the number at current index not equal to largest number
        if index_num_dict[i] != max_number:
            # find the index of the largest number 
            index_max_number = num_index_dict[max_number]
            # swap the value of the largest number with value of current index
            index_num_dict[index_max_number] = index_num_dict[i]
            # swap the index of the current number with index of the largest number    
            num_index_dict[index_num_dict[i]] = index_max_number 
            # swap the number of the current index with the largest number
            index_num_dict[i] = max_number
            # update the swap parameter
            k -= 1
        # update the largest number
        max_number -= 1
        # update the current index
        i += 1
    # return the largest permutation 
    return index_num_dict.values()
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
