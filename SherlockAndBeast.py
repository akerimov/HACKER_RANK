#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Sherlock Holmes suspects his archenemy Professor Moriarty is once again plotting something diabolical. 
Sherlock's companion, Dr. Watson, suggests Moriarty may be responsible for MI6's recent issues with their 
supercomputer, The Beast. Shortly after resolving to investigate, Sherlock receives a note from Moriarty 
boasting about infecting The Beast with a virus. He also gives him a clue: an integer. Sherlock determines 
the key to removing the virus is to find the largest Decent Number having that number of digits.

A Decent Number has the following properties:
    (1) Its digits can only be 3's and/or 5's.
    (2) The number of 3's it contains is divisible by 5.
    (3) The number of 5's it contains is divisible by 3.
    (4) It is the largest such number for its length.

Function Description:
Complete the decentNumber function below.

decentNumber has the following parameter(s):
INPUT:
    int n: the length of the decent number to create
OUTPUT:
    Print the decent number for the given length, or  -1 if a decent number of that length cannot be formed. 

Link to problem statement:
https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'decentNumber' function below.
The function accepts INTEGER n as parameter.
Returns INTEGER 

Link to problem statement:
https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
"""

def decentNumber(n):
    #there is no Decent Number having  digit
    if n == 1:
        return -1
    
    # initialize count of digit 3s
    count_digit_three = 0
    # start from "5"*n number and keep adding "3" from the end
    while count_digit_three<=n:
        # update the number by adding "3" from the end
        number = "5"*(n-count_digit_three) + "3"*count_digit_three
        #print(number)
        # check if Decent Number properties are satified
        if ((n-count_digit_three) %3 == 0) and (count_digit_three % 5 ==0):
            # return Decent Number
            return int(number)
        # update count of digit 3s 
        count_digit_three += 1
    
    #  return -1 if a decent number of n length cannot be formed
    return -1 
           
    
if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        print(decentNumber(n))

