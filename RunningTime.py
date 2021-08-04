#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Can you modify your previous Insertion Sort implementation to keep track of the number of 
shifts it makes while sorting? The only thing you should print is the number of shifts made 
by the algorithm to completely sort the array. A shift occurs when an element's position 
changes in the array. Do not shift an element if it is not necessary.

Function Description:
Complete the runningTime function below.
runningTime has the following parameter:
INPUT:
    int arr[n]: an array of integers
OUTPUT:
    int: the number of shifts it will take to sort the array
    
Link to problem statement:
https://www.hackerrank.com/challenges/runningtime/problem
"""


# In[ ]:


#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'runningTime' function below.
The function is expected to return an INTEGER.
The function accepts INTEGER_ARRAY arr as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/runningtime/problem
"""

def runningTime(arr):
    total_shifts = 0
    for i in range(1, len(arr)):
        shifts = 0
        target_num = arr[i]
        j = i -1
        while j>=0 and (arr[j] > target_num):
            arr[j+1] = arr[j]
            j -= 1
            shifts += 1
        arr[j+1] = target_num
        #print(shifts, arr)
        total_shifts += shifts
    return total_shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = runningTime(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

