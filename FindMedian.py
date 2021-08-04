#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
The median of a list of numbers is essentially its middle element after sorting. 
The same number of elements occur after it as before. Given a list of numbers with 
an odd number of elements, find the median?

Function Description:
Complete the findMedian function below.
findMedian has the following parameter:
INPUT:
    int arr[n]: an unsorted array of integers
OUTPUT:
    int: the median of the array
    
Link to problem statement:
https://www.hackerrank.com/challenges/find-the-median/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'findMedian' function below.
The function is expected to return an INTEGER.
The function accepts INTEGER_ARRAY arr as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/find-the-median/problem
"""

def findMedian(arr):
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
        
    # find median by slicing the middle element
    median = sorted_arr[len(arr)//2]
    return median
    
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    arr = list(map(int, input().rstrip().split()))
#    result = findMedian(arr)
#    fptr.write(str(result) + '\n')
#    fptr.close()

