#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Reduce a string of lowercase characters in range ascii[‘a’..’z’] by doing a 
series of operations. In each operation, select a pair of adjacent letters that 
match, and delete them.  Delete as many characters as possible using this method 
and return the resulting string. If the final string is empty, return Empty String.

Function Description:
Complete the superReducedString function below.

superReducedString has the following parameter:
INPUT:    
    string s: a string to reduce
OUTPUT:
    string: the reduced string or Empty String
    
Link to problem statement: 
https://www.hackerrank.com/challenges/reduced-string/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'superReducedString' function below.
The function is expected to return a STRING.
The function accepts STRING s as parameter.

Link to problem statement: 
https://www.hackerrank.com/challenges/reduced-string/problem
"""

def superReducedString(s):
    match = re.findall(r'((\w)\2)', s)
    while match: 
        for group in match:
            s = s.replace(group[0], "")
            print(s) 
        match = re.findall(r'((\w)\2)', s)
    
    if len(s) == 0:
        return "Empty String"
    return s

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    s = input()
#    result = superReducedString(s)
#    fptr.write(result + '\n')
#    fptr.close()

