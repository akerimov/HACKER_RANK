#!/usr/bin/env python
# coding: utf-8

"""
Two words are anagrams of one another if their letters can be rearranged to form the other word.
Given a string, split it into two contiguous substrings of equal length. Determine the minimum 
number of characters to change to make the two substrings into anagrams of one another.

Complete the anagram function below.
anagram has the following parameter:
INPUT:
    string s: a string
OUTPUT:
    int: the minimum number of characters to change or -1.
    
Link to problem statement:
https://www.hackerrank.com/challenges/anagram/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'anagram' function below.
The function is expected to return an INTEGER.
The function accepts STRING s as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/anagram/problem
"""

def anagram(s):
    # Write your code here
    if len(s) % 2 != 0:
        min_ch = -1
    else: 
        left_s = list(s[:len(s)//2])
        right_s = list(s[len(s)//2:])
        min_ch = 0
        for ch in right_s:
            if ch in left_s:
                left_s.remove(ch)
            else:
                min_ch += 1
    return min_ch      

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    q = int(input().strip())
#
#    for q_itr in range(q):
#        s = input()
#        result = anagram(s)
#        fptr.write(str(result) + '\n')
#    fptr.close()
