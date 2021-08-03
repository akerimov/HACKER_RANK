#!/usr/bin/env python
# coding: utf-8

"""
Given a string, remove characters until the string is made up of any two alternating characters. 
When you choose a character to remove, all instances of that character must be removed. Determine 
the longest string possible that contains just two alternating letters.


Function Description:
Complete the alternate function below.
alternate has the following parameters:

INPUT:
    string s: a string
OUTPUT:
    int: the length of the longest valid string, or  if there are none
    
Link to problem statement: 
https://www.hackerrank.com/challenges/two-characters/problem
"""


#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from itertools import combinations

"""
Complete the 'alternate' function below.
The function is expected to return an INTEGER.
The function accepts STRING s as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/two-characters/problem
"""

def alternate(s):
    
    # some edge cases
    if len(s)<2 or s[0]==s[1]:
        return 0
    elif len(s) == 2 and s[0]!=s[1]:
        return 2
    
    # create the combinations of letters to be removed from s
    letters = list(Counter(s).keys())
    letters_combinations_remove = combinations(letters,len(letters)-2)
    
    # resulting strings after removing the combination of letters from s
    two_characters_strings = []
    for combination in letters_combinations_remove:
        #print(combination)
        s_short = s
        for ch in combination:
            s_short = s_short.replace(ch,"")
        two_characters_strings.append(s_short)
            
    # create the list of strings with alternate characters only
    two_characters_strings_special = two_characters_strings.copy()
    for item in two_characters_strings: 
        
        if item[0] == item[1]:
            two_characters_strings_special.remove(item)
            continue 
        
        for index in range(len(item)-2):
            if item[index] != item[index+2]:
                two_characters_strings_special.remove(item)
                break
    if two_characters_strings_special:
        return len(max(two_characters_strings_special, key=len))
    else:
        return 0

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    l = int(input().strip())
#    s = input()
#    result = alternate(s)
#    fptr.write(str(result) + '\n')
#    fptr.close()
