#!/usr/bin/env python
# coding: utf-8

"""
James found a love letter that his friend Harry has written to his girlfriend. 
James is a prankster, so he decides to meddle with the letter. He changes all 
the words in the letter into palindromes.

To do this, he follows two rules:
    (1) He can only reduce the value of a letter by 1 , i.e. he can change d to c, 
        but he cannot change c to d or d to b.
    (2) The letter a  may not be reduced any further.

Each reduction in the value of any letter is counted as a single operation. 
Find the minimum number of operations required to convert a given string into a palindrome.

Function Description
Complete the theLoveLetterMystery function below.
theLoveLetterMystery has the following parameter(s):
INPUT:
    string s: the text of the letter
OUTPUT:
    int: the minimum number of operations

Link to problem statement:
https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'theLoveLetterMystery' function below.
The function is expected to return an INTEGER.
The function accepts STRING s as parameter.

Link to peroblem statement:
https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
"""

def theLoveLetterMystery(s):
    # initialize alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # string s is palindrome if its reversed left substring is equal to right  substring   
    # split the input string into left and right part
    s_left = s[:(len(s)//2)]
    s_left_inv = s_left[::-1]
    if len(s) % 2 ==0:
        s_right = s[len(s)//2:]
    else:
        s_right = s[len(s)//2+1:]
    #print(s_left, s_left_inv, s_right)
    
    # initialize the minimum operations 
    min_operations = 0
    # loop over the index in the right substring of s
    for index in range(len(s_right)):
        # check if the letter at current index are not the same 
        # in the reversed left and right substrings
        if s_right[index] != s_left_inv[index]:
            # compute the alphabet index differences between the letters in both substrings 
            diff = alphabet.find(s_right[index]) - alphabet.find(s_left_inv[index])
            # update the minimum number of operations
            min_operations += abs(diff)
    return min_operations 
                
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = theLoveLetterMystery(s)
        fptr.write(str(result) + '\n')
    fptr.close()
