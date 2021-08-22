#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Two people are playing Nimble! The rules of the game are:
    (1) The game is played on a line of  n squares.  Each square contains i coins. 
    (2) The players move in alternating turns. During each move, the current player 
        must remove exactly 1 coin from square i and move it to square j if and only if 0<=j<i.
    (3) The game ends when all coins are in square 0 and nobody can make a move. 
        The first player to have no available move loses the game.

Given the value of n and the number of coins in each square, determine whether the person 
who wins the game is the first or second person to move. Assume both players move optimally.

Link to problem statement:
https://www.hackerrank.com/challenges/nimble-game-1/problem
"""


# In[ ]:


#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'nimbleGame' function below.
The function is expected to return a STRING.
The function accepts INTEGER_ARRAY s as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/nimble-game-1/problem
"""

def nimbleGame(s):
    # The nimble game can be decoded as list of piles. 
    # Piles in each square have the same size. Then, 
    # the problem is reduced to a nim game problem.

    # compute the nim-sum
    nim_sum = 0
    for index in range(len(s)):
        # ignore the squares with even coins
        if s[index]%2 >0:
            # add the index (e.g.,pile size) to the nim-sum
            nim_sum ^= index
    # check if nim-sum is zero
    if nim_sum == 0:
        return "Second"
    return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        s = list(map(int, input().rstrip().split()))
        result = nimbleGame(s)
        fptr.write(result + '\n')
    fptr.close()

