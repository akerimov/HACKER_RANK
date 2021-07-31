#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of 
this conspiracy from Raven and plans to lock the single door through which the enemy 
can enter his kingdom. But, to lock the door he needs a key that is an anagram of a 
palindrome. He starts to go through his box of strings, checking to see if they can 
be rearranged into a palindrome. Given a string, determine if it can be rearranged 
into a palindrome. Return the string YES or NO.

Complete the gameOfThrones function below.
gameOfThrones has the following parameters:
INPUT:
    string s: a string to analyze
OUTPUT:
    string: either YES or NO
    
Link to problem statement:
https://hpcjupyter.hpc.pce.bp.com/user/karia3/lab?
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
Complete the 'gameOfThrones' function below.
The function is expected to return a STRING.
The function accepts STRING s as parameter.

Link to problem statement:
https://hpcjupyter.hpc.pce.bp.com/user/karia3/lab?
"""

def gameOfThrones(s):
    warning = 0
    counts = Counter(s)
    for ch in counts:
        if counts[ch] % 2 != 0:
            warning += 1
    if warning > 1:
        return "NO"
    return "YES" 
    
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    s = input()
#    result = gameOfThrones(s)
#    fptr.write(result + '\n')
#    fptr.close()

