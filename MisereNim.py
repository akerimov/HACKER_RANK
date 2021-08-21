#!/usr/bin/env python
# coding: utf-8

"""
Two people are playing game of Misère Nim. The basic rules for this game are as follows:
    (1) The game starts with n piles of stones. Each pile has si stones.
    (2) The players move in alternating turns. During each move, the current 
        player must remove one or more stones from a single pile.
    (3) The player who removes the last stone loses the game.

Given the value of n and the number of stones in each pile, determine whether the person 
who wins the game is the first or second person to move. If the first player to move wins, 
print First on a new line; otherwise, print Second. Assume both players move optimally.

Function Description
Complete the misereNim function below.
misereNim has the following parameters:
INPUT:
    int s[n]: the number of stones in each pile
OUTPUT:
    string: either First or Second

Link to problem statement: 
https://www.hackerrank.com/challenges/poker-nim-1/problem
"""


#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'misereNim' function below.
The function is expected to return a STRING.
The function accepts INTEGER_ARRAY s as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/misere-nim-1/problem
"""

def misereNim(s):
    # compute the nim sum between the piles
    nim_sum = 0
    for num in s:
        nim_sum ^= num
    
    # check if number of piles is even and consists of 1 stones 
    if (len(s) %2 == 0 and (s.count(1) == len(s))):
        return "First"
    
    # check if number of piles is odd and consists of 1 stones
    if len(s) %2 != 0 and (s.count(1) == len(s)):
        return "Second"
    
    # check if nim sum is greater than zero    
    if nim_sum > 0:
        return "First"
    
    return "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        s = list(map(int, input().rstrip().split()))
        result = misereNim(s)
        fptr.write(result + '\n')
    fptr.close()
