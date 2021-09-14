#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. 
In other words, both strings must contain the same exact letters in the same exact frequency. For example, bacdc and dcbac are 
anagrams, but bacdc and dcbad are not.

Alice is taking a cryptography class and finding anagrams to be very useful. She decides on an encryption scheme involving two 
large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. 
Can you help her find this number? Given two strings,  s1 and s2, that may not be of the same length, determine the minimum number 
of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

Function Description
Complete the makingAnagrams function below.
makingAnagrams has the following parameter(s):
INPUT: 
    string s1: a string
    string s2: a string
OUTPUT:
    int: the minimum number of deletions needed

Link to problem statement:
https://www.hackerrank.com/challenges/making-anagrams/problem
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
Complete the 'makingAnagrams' function below.
The function is expected to return an INTEGER.
The function accepts following parameters:
  1. STRING s1
  2. STRING s2
  
Link to problem statement:
https://www.hackerrank.com/challenges/making-anagrams/problem
"""

def makingAnagrams(s1, s2):
    
    # create the letter count dictionaries:
    # where key=letter, value = count
    s1 = Counter(s1)
    s2 = Counter(s2)
    
    # loop over the letters in s1
    for ch in s1:
        # check if a current letter exist in s2 
        if ch in s2:
            # add the current letter withvdiff between counts to s2
            s2[ch] =  abs(s2[ch] - s1[ch])
        else:
            # add the current letter with its count to s2
            s2[ch] = s1[ch]
    
    # find the number of deletions needed to make anagram
    num_deletions = sum(s2.values())
    return num_deletions 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = makingAnagrams(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()

