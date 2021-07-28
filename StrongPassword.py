#!/usr/bin/env python
# coding: utf-8

"""
Louise joined a social networking site to stay in touch with her friends. 
The signup page required her to input a name and a password. However, the 
password must be strong. The website considers a password to be strong if 
it satisfies the following criteria:

    (1) Its length is 6 at least .
    (2) It contains at least one digit.
    (3) It contains at least one lowercase English character.
    (4) It contains at least one uppercase English character.
    (5) It contains at least one special character. The special characters are: !@#$%^&*()-+

She typed a random string of length  in the password field but wasn't sure 
if it was strong. Given the string she typed, can you find the minimum number 
of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"

Function Description
Complete the minimumNumber function below.

minimumNumber has the following parameters:
INPUT:
    int n: the length of the password
    string password: the password to test
OUPUT:
    int: the minimum number of characters to add

Link to problem statement:
https://www.hackerrank.com/challenges/strong-password/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'minimumNumber' function below.

The function is expected to return an INTEGER.
The function accepts following parameters:
    INTEGER n
    STRING password
"""

def minimumNumber(n, password): 
    regex = ['[!@#$%^&*()\-\+]', '[a-z]', '[A-Z]', '[\d]']
    count = 0
    for r in regex:
        if not bool(re.search(r,password)):
            count += 1
    
    if n >= 6 and count>=0:
        return count 
    elif n < 6 and count > (6-n):
        return count
    else: 
        return 6-n
    
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    password = input()
#    answer = minimumNumber(n, password)
#    fptr.write(str(answer) + '\n')
#    fptr.close()

