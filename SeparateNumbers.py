#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
A numeric string, s, is beautiful if it can be split into a sequence of two or more positive integers, 
a[1], a[2], ..., a[n] satisfying the following conditions:
    (1) a[i] - a[i-1] = 1 for 1 < i <-n
    (2) No a[i] contains a leading zero. For example, we can split s=10203 into {1,02,03}, 
        but it is not beautiful because 02 and 03 have leading zeros
    (3) The contents of the sequence cannot be rearranged. For example, we can split s=312 
        into the sequence {3,1,2}, but it is not beautiful because it breaks our first constraint 
        (i.e., 1-3 is not 1 ).

Function Description:
Complete the separateNumbers function below.
separateNumbers has the following parameter:
INPUT:
    s: an integer value represented as a string
OUTPUT:
    string: Print a string as described above. Return nothing.
    
Link to problem statement:
https://www.hackerrank.com/challenges/separate-the-numbers/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
# Complete the 'separateNumbers' function below.
# The function accepts STRING s as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/separate-the-numbers/problem
"""

def separateNumbers(s):
    flag = "NO"
    for i in range(len(s)//2):
        if int(s[:i+1][0]) == 0:
            continue
        else: 
            first_num = int(s[:i+1])     
           
        beautiful_s = str(first_num)
        next_num = first_num + 1
        while len(beautiful_s) <= len(s) - len(str(next_num)):
            beautiful_s += str(next_num)
            next_num += 1
        
        if beautiful_s == s:
            flag  = "YES " + str(first_num)
            break 
    print(flag)
        
                
if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        separateNumbers(s)

