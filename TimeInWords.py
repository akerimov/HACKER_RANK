#!/usr/bin/env python
# coding: utf-8

"""
Given the time in numerals we may convert it into words, as shown below:
At minutes=0, use o' clock. For 1<=minutes<=30, use past, and for 30<minutes use to. 
Note the space between the apostrophe and clock in o' clock. Write a program which 
prints the time in words for the input given in the format described.

Function Description
Complete the timeInWords functionbelow.
timeInWords has the following parameter(s):
INPUT:
    int h: the hour of the day
    int m: the minutes after the hour
OUTPUT:
string: a time string as described

Link to problem statement:
https://www.hackerrank.com/challenges/the-time-in-words/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys


"""
Complete the 'timeInWords' function below.
The function is expected to return a STRING.
The function accepts following parameters:
  1. INTEGER h
  2. INTEGER m
  
Link to problem statement:
https://www.hackerrank.com/challenges/the-time-in-words/problem
"""

def timeInWords(h, m):
    # define the dictionary: key=numerals, value = words
    num2word = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',              
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',             
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',            
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',             
                19: 'nineteen', 20: 'twenty', 21: 'twenty one', 22: 'twenty two',            
                23: 'twenty three', 24: 'twenty four', 25: 'twenty five',            
                26: 'twenty six', 27: 'twenty seven', 28: 'twenty four',            
                29: 'twenty nine', 30: 'thirty', 0: 'zero'}
    
    # check if 00 minutes return o' clock
    if m == 0:
        hour = num2word[h]
        time_in_words = hour + " o' clock"  
    # check if half past an hour
    elif m == 30: 
        hour = num2word[h]
        time_in_words = "half past " + hour
    else:
        # check if minutes less than or equal to 30 
        if m<=30 :
            hour = num2word[h]
            minutes = num2word[m]
            # check the quarter past an hour
            if m == 15:
                time_in_words = "quarter past " + hour 
            # check one minute past an hour 
            elif m == 1:
                time_in_words = minutes + " minute past " + hour 
            # check >1 minutes past an hour
            else:
                time_in_words = minutes + " minutes past " + hour 
        else:      
            hour = num2word[h+1]
            minutes = num2word[60-m]
            # check if the quarter to an hour
            if (60-m) == 15:
                time_in_words = "quarter to " + hour
            # check if one minute to an hour  
            elif (60-m) == 1:
                time_in_words = minutes + " minute to " + hour 
            # check if >1 minutes to an hour
            else:
                time_in_words = minutes + " minutes to " + hour 
    return time_in_words
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    fptr.write(result + '\n')
    fptr.close()
