#!/usr/bin/env python
# coding: utf-8

"""
Priyanka works for an international toy company that ships by container. Her task is to 
the determine the lowest cost way to combine her orders for shipping. She has a list of 
item weights. The shipping company has a requirement that all items loaded in a container 
must weigh less than or equal to 4 units plus the weight of the minimum weight item. All 
items meeting that requirement will be shipped in one container.What is the smallest number 
of containers that can be contracted to ship the items based on the given list of weights? 

Function Description:
Complete the toys function below.
toys has the following parameter:
INPUT:
    w: an array of integers that represent the weights of each order to ship
OUTPUT:
    the integer value of the number of containers Priyanka must contract to ship all of the toys.
    
Link to problem statement:
https://www.hackerrank.com/challenges/mark-and-toys/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'toys' function below.
The function is expected to return an INTEGER.
The function accepts INTEGER_ARRAY w as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/priyanka-and-toys/problem
"""

def toys(w):
    # sort the weights in ascemding order
    w.sort(reverse=False)
    # find the max weight for a given container
    max_weight = min(w) + 4 
    # initialize container
    countainers = 1 
    # loop over each weight
    for weight in w: 
        # check if weight is greater than the max weight for a given container 
        if weight>max_weight:
            # update the maxixumem weight for next container
            max_weight = weight + 4
            # update the container
            countainers +=1
    # return number of containers
    return countainers

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    w = list(map(int, input().rstrip().split()))
    result = toys(w)
    fptr.write(str(result) + '\n')
    fptr.close()
