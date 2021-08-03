#!/usr/bin/env python
# coding: utf-8

"""
A pangram is a string that contains every letter of the alphabet. 
Given a sentence determine whether it is a pangram in the English alphabet. 
Ignore case. Return either pangram or not pangram as appropriate.

Function Description
Complete the function pangrams ibelow. It should return the string pangram 
if the input string is a pangram. Otherwise, it should return not pangram.

pangrams has the following parameters:
INPUT:
    string s: a string to test
OUTPUT:
    string: either pangram or not pangram
    
Link to problem statement:
https://www.hackerrank.com/challenges/pangrams/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'pangrams' function below.
The function is expected to return a STRING.
The function accepts STRING s as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/pangrams/problem
"""

def pangrams(s):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
                'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p', 'q', 'r', 's', 't', 'u', 
                'v', 'w', 'x', 'y', 'z']

    for ch in alphabet:
        if ch not in s.lower():
            return "not pangram"
    return "pangram"
        
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    s = input()
#    result = pangrams(s)
#    fptr.write(result + '\n')
#    fptr.close()
