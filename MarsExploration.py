#!/usr/bin/env python
# coding: utf-8

"""
A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
Letters in some of the SOS messages are altered by cosmic radiation during transmission. 
Given the signal received by Earth as a string, , determine how many letters of the SOS 
message have been changed by radiation.

Function Description:
Complete the marsExploration function  below.

marsExploration has the following parameter:
INPUT: 
    string s: the string as received on Earth
output:
    int: the number of letters changed during transmission

Link to problem statement:
https://www.hackerrank.com/challenges/mars-exploration/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys

"""
Link to problem statement:
https://www.hackerrank.com/challenges/mars-exploration/problem

Complete the 'marsExploration' function below.
The function is expected to return an INTEGER.
The function accepts STRING s as parameter.
"""

def marsExploration(s):
    mistakes = 0
    expected_s = "SOS"*len(s)
    for idx, ch in enumerate(s):
        if ch != expected_s[idx]:
            mistakes += 1
    return mistakes

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    s = input()
#    result = marsExploration(s)
#    fptr.write(str(result) + '\n')
#    fptr.close()

