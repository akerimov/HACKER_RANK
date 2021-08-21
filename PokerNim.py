#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Poker Nim is another -player game that's a simple variation on a Nim game. 
The rules of the games are as follows:
    (1) The game starts with n piles of chips. Each pile  (where ) has ci chips.
    (2) The players move in alternating turns. During each move, the current player must 
        perform either of the following actions:
        - Remove one or more chips from a single pile.
        - Add one or more chips to a single pile.
    (3) At least 1 chip must be added or removed during each turn.
    (4) To ensure that the game ends in finite time, a player cannot
        add chips to any pile  more than  times.
    (5) The player who removes the last chip wins the game.

Given the values of n, k, and the numbers of chips in each of the n piles, 
determine whether the person who wins the game is the first or second person to move. 
Assume both players move optimally.

Link to problem statement: 
https://www.hackerrank.com/challenges/poker-nim-1/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'pokerNim' function below.
The function is expected to return a STRING.
The function accepts following parameters:
  1. INTEGER k
  2. INTEGER_ARRAY c

Link to problem statement:
https://www.hackerrank.com/challenges/poker-nim-1/problem
"""

def pokerNim(k, c):
    # the winning strategy is to finish every move with a nim-sum of 0
    # Find a pile where the nim-sum of all piles and given pile-size is 
    # less than the given pilen-size; the winning strategy is to play 
    # in such a pile, reducing that pile to the nim-sum of its original 
    # size with nim-sim of all piles
    
    # compute nim-sum between piles
    xor = 0
    for p in c:
        xor ^= p     
    # check if num-sum is zero
    if xor ==0:
        return "Second"
    return "First"
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        c = list(map(int, input().rstrip().split()))
        result = pokerNim(k, c)
        fptr.write(result + '\n')
    fptr.close()

