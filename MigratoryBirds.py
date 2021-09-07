#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Given an array of bird sightings where every element represents a bird type id, 
determine the id of the most frequently sighted type. If more than 1 type has 
been spotted that maximum amount, return the smallest of their ids.

Function Description
Complete the migratoryBirds function below.
migratoryBirds has the following parameter(s):
INPUT:
    int arr[n]: the types of birds sighted
OUTPUT:
    int: the lowest type id of the most frequently sighted birds

Link to problem statement:
https://www.hackerrank.com/challenges/migratory-birds/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

"""
Complete the 'migratoryBirds' function below.
The function is expected to return an INTEGER.
The function accepts INTEGER_ARRAY arr as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/migratory-birds/problem
"""

def migratoryBirds(arr):
    # create the dictionary: key = id, value = count
    id_count = Counter(arr) 
    # create an empty reversed dictionary: key = count, value = ids
    count_ids = {}
    # loop over the key, value in id_count
    for ids, count in id_count.items():
        # check if current count exist in flipped dictionary
        if count in count_ids:
            # update list of ids with current count in flipped dict
            count_ids[count].append(ids)
        else:
            # update list of ids with current count in flipped dict
            count_ids[count] = [ids]
    # find maximum number of counts
    max_count = max(count_ids.keys())
    # return least frequent of most frequently ids
    return min(count_ids[max_count])
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()

