#!/usr/bin/env python
# coding: utf-8

"""
There is a sequence of words in CamelCase as a string of letters, s, having the following properties:
    (1) It is a concatenation of one or more words consisting of English letters.
    (2) All letters in the first word are lowercase.
    (3) For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.

Given s, determine the number of words in s.

Function Description:
Complete the camelcase function below.

camelcase has the following parameters:
INPUT:
    string s: the string to analyze
OUTPUT
    int: the number of words in s 
    
Link to the problem statement:
https://www.hackerrank.com/challenges/camelcase/problem
"""


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Link to the problem statement:
https://www.hackerrank.com/challenges/camelcase/problem

# Complete the 'camelcase' function below.
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
"""

def camelcase(s):
    count = 1
    for idx, ch in enumerate(s):
        if ch.isupper():
            count +=1
    return count
            
        
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    s = input()
#    result = camelcase(s)
#    fptr.write(str(result) + '\n')
#    fptr.close()

