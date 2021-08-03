#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Often, when a list is sorted, the elements being sorted are just keys to other values. 
For example, if you are sorting files by their size, the sizes need to stay connected 
to their respective files. You cannot just take the size numbers and output them in 
order, you need to output all the required file information. The counting sort is used 
if you just need to sort a list of integers. Rather than using a comparison, you create 
an integer array whose index range covers the entire range of values in your array to 
sort. Each time a value occurs in the original array, you increment the counter at that 
index. At the end, run through your counting array, printing the value of each non-zero 
valued index that number of times. Given an unsorted list of integers, use the counting 
sort method to sort the list and then print the sorted list.

Function Description:
Complete the countingSort function below.
countingSort has the following parameters:
INPUT:
    arr[n]: an array of integers
OUTPUT:
    arr[n]: print the sorted list as a single line of space-separated integers.
    
Link to problem statement:
https://www.hackerrank.com/challenges/countingsort1/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
# Complete the 'countingSort' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/countingsort1/problem
"""

def countingSort(arr):
    # create an empty number frequency array
    count_arr = [0] * (max(arr)+2)
    # loop over the numbers in arr
    for num in arr:
        # update the frequency of number
        count_arr[num] += 1
    
    # loop over the indices of frequency array
    sorted_arr = []
    for index in range(0, len(count_arr)):
        # use the counts to add the number 
        sorted_arr.extend([index]*count_arr[index])
    
    # return sorted array
    return sorted_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

