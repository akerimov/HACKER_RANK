#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread. Your subjects are in a line, 
and some of them already have some loaves. Times are hard and your castle's food stocks are dwindling, so you must 
distribute as few loaves as possible according to the following rules:

(1) Every time you give a loaf of bread to some person , you must also give a loaf of bread to the person immediately 
in front of or behind them in the line (i.e., persons i or i+1).
(2) After all the bread is distributed, each person must have an even number of loaves. 

Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must distribute 
to satisfy the two rules above. If this is not possible, print NO.

Function Description
Complete the fairRations function below:.
fairRations has the following parameter(s):
INPUT: 
    int B[N]: the numbers of loaves each persons starts with
RETURNS
    string: the minimum number of loaves required, cast as a string, or 'NO'

Link to problem statement:
https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'fairRations' function below.
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.

def fairRations(B):
    # initialize number of loaves
    num_loaves = 0
    
    # loop over the people
    for index in range(len(B)-1):
        
        # check if the current person has an odd number of loaves
        if B[index] %2 != 0:
            # update the number of loaves of the current person
            B[index] += 1
            # update the number of loaves of the next person
            B[index+1] +=1
            # update the total number of given loabes
            num_loaves += 2
    
    # check if all people have the even number of loaves
    if sum(B) % 2 == 0:
        return str(num_loaves)
    return "NO"
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    N = int(input().strip())
    B = list(map(int, input().rstrip().split()))
    result = fairRations(B)
    fptr.write(result + '\n')
    fptr.close()

