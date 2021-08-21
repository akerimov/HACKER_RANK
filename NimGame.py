#!/usr/bin/env python
# coding: utf-8

"""
Nim is the most famous two-player algorithm game. The basic rules for this game are as follows:
    (1) The game starts with a number of piles of stones. The number of stones in each 
        pile may not be equal.
    (2) The players alternately pick up 1 or more stones from 1 pile
    (3) The player to remove the last stone wins.

Given the value of n and the number of stones in each pile, determine the game's winner 
if both players play optimally.

Function Desctription
Complete the nimGame function below. 
nimGame has the following parameter(s):
INPUT:
    pile: an integer array that represents the number of stones in each pile
OUTPUT:
    It should return a string, either First or Second.

Link to problem statement: 
https://www.hackerrank.com/challenges/nim-game-1/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'nimGame' function below.
The function is expected to return a STRING.
The function accepts INTEGER_ARRAY pile as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/nim-game-1/problem
"""

def nimGame(pile):
    # compute the nim-sum between piles
    xor = 0
    for p in pile:
        xor ^= p        
    # check if num-sum is zero
    if xor == 0:
        return "Second"
    return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    g = int(input().strip())
    for g_itr in range(g):
        n = int(input().strip())
        pile = list(map(int, input().rstrip().split()))
        result = nimGame(pile)
        fptr.write(result + '\n')
    fptr.close()
