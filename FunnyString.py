#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
In this challenge, you will determine whether a string is funny or not. To determine whether 
a string is funny, create a copy of the string in reverse e.g. abc to cba. Iterating through 
each string, compare the absolute difference in the ascii values of the characters at positions 
0 and 1, 1 and 2 and so on to the end. If the list of absolute differences is the same for both 
strings, they are funny. Determine whether a give string is funny. If it is, return Funny,
otherwise return Not Funny.

Complete the funnyString function below.
funnyString has the following parameter:
INPUT: 
    string s: a string to test
OUPUT: 
    string: either Funny or Not Funny
    
Link to problem statement:
https://www.hackerrank.com/challenges/funny-string/problem
"""


# In[ ]:


#!/bin/python3
import math
import os
import random
import re
import sys

""" 
Complete the 'funnyString' function below.
The function is expected to return a STRING.
The function accepts STRING s as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/funny-string/problem
"""

def funnyString(s):
    # Write your code here
    s_ascii = [ord(ch) for ch in s]
    s_reverse_ascii = [ord(ch) for ch in s[::-1]]
    
    if [abs(s_ascii[i] - s_ascii[i+1]) for i in range(len(s_ascii)-1)] == [abs(s_reverse_ascii[i] - s_reverse_ascii[i+1]) for i in range(len(s_reverse_ascii)-1)]:
        return 'Funny'
    else:
        return "Not Funny"

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    q = int(input().strip())
#    for q_itr in range(q):
#        s = input()
#        result = funnyString(s)
#        fptr.write(result + '\n')
#    fptr.close()

