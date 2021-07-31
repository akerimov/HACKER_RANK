#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Given a string of lowercase letters in the range ascii[a-z], determine the index of a character 
that can be removed to make the string a palindrome. There may be more than one solution, but any 
will do. If the word is already a palindrome or there is no solution, return -1. Otherwise, return 
the index of a character to remove.

Complete the palindromeIndex function below.
palindromeIndex has the following parameters:
INPUT: 
    string s: a string to analyze
OUTPUT:
    int: the index of the character to remove or -1
    
Link to problem statetment:
https://www.hackerrank.com/challenges/palindrome-index/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'palindromeIndex' function below.
The function is expected to return an INTEGER.
The function accepts STRING s as parameter.

Link to problem statetment:
https://www.hackerrank.com/challenges/palindrome-index/problem
"""

def palindromeIndex(s): 
    s = list(s)
    for index in range(len(s)//2):     
        if s[index] == s[len(s)-1-index]:
            continue
        else: 
            s.pop(index)
            if s == s[::-1]:
                return index
            else:
                return len(s)-index
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = palindromeIndex(s)
        fptr.write(str(result) + '\n')
    fptr.close()

