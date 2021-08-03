#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Another sorting method, the counting sort, does not require comparison. 
Instead, you create an integer array whose index range covers the entire 
range of values in your array to sort. Each time a value occurs in the 
original array, you increment the counter at that index. At the end, run 
through your counting array, printing the value of each non-zero valued 
index that number of times. Given a list of integers, count and return the 
number of times each value appears as an array of integers.

Function Description:
Complete the countingSort function below.
countingSort has the following parameters:
INPUT:
    arr[n]: an array of integers
OUTPUT:
    int[100]: a frequency array
    
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
        
    #sorted_arr = []
    #for index in range(1, len(count_arr)):
    #    sorted_arr.extend([index]*count_arr[index])
    
    # return firts 100 numbers
    return count_arr[0:100]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

