#!/usr/bin/env python
# coding: utf-8

"""
Our local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). 
The fee structure is as follows:
    (1) If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0) .
    (2) If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine = 15 x (number of later days) .
    (3) If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine = 500 x (number of late months).
    (4) If the book is returned after the calendar year in which it was expected, there is a fixed fine of 1000.

Function Description
Complete the libraryFine function below.
libraryFine has the following parameter(s):
INPUT:
    d1, m1, y1: returned date day, month and year, each an integer
    d2, m2, y2: due date day, month and year, each an integer
OUTPUT:
    int: the amount of the fine or  if there is none

Link to problem statement:
https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
#Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#
# Link to problem statement:
# https://www.hackerrank.com/challenges/library-fine/problem?isFullScreen=true
"""

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1>y2:
        fine = 10000*(y1-y2)
    elif m1>m2 and y1==y2:
        fine = 500*(m1-m2)
    elif d1>d2 and m1==m2 and y1==y2:
        fine = 15*(d1-d2)
    else:
        fine = 0    
    return fine 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    d1 = int(first_multiple_input[0])
    m1 = int(first_multiple_input[1])
    y1 = int(first_multiple_input[2])
    second_multiple_input = input().rstrip().split()
    d2 = int(second_multiple_input[0])
    m2 = int(second_multiple_input[1])
    y2 = int(second_multiple_input[2])
    result = libraryFine(d1, m1, y1, d2, m2, y2)
    fptr.write(str(result) + '\n')
    fptr.close()

