#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value that describe a range of integers, 
inclusive of the endpoints. Sherlock must determine the number of square integers within that range.

Function Description
Complete the squares function below.
It should return an integer representing the number of square integers in the inclusive range from  a to b.

squares has the following parameter(s):
INPUT:
    int a: the lower range boundary
    int b: the upper range boundary
RETURNS:
    int: the number of square integers in the range

Link to problem statement:
https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys
import math

# Complete the 'squares' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#
# Link to problem statement:
# https://www.hackerrank.com/challenges/sherlock-and-squares/problem?isFullScreen=true

def squares(a, b):
    # initialize the list of squares
    list_squares = []
    
    # find the first number that create the square numbwe between a and b
    num = math.ceil(math.sqrt(a))
    
    # loop over the num +1 as long as num**2 less than or equal to b 
    while num**2 <= b:
        # append the square number into the list  
        list_squares.append(num**2)
        # update the number by +1 
        num +=1   
    # return the count of square numbers between a and b
    return len(list_squares)
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()
        a = int(first_multiple_input[0])
        b = int(first_multiple_input[1])
        result = squares(a, b)
        fptr.write(str(result) + '\n')
    fptr.close()

