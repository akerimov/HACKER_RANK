#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Two players called  P1 and P2 are playing a game with a starting number of stones. 
Player 1 always plays first, and the two players move in alternating turns. 
The game's rules are as follows:

    In a single move, a player can remove either 2,3,5 or  stones from the game board.
    If a player is unable to make a move, that player loses the game.
    
Given the starting number of stones, find and print the name of the winner. 
p1 is named First and P2 is named Second. Each player plays optimally, meaning 
they will not make a move that causes them to lose the game if a winning move exists.

Function Description:
Complete the gameOfStones function below.
It should return a string, either First or Second.

gameOfStones has the following parameter(s):
INPUT: 
    n: an integer that represents the starting number of stones
OUTPUT: 
    n a new line for each test case, print First if the first player is the winner. 
    Otherwise print Second.  
      
Link to problem statement:
https://www.hackerrank.com/challenges/game-of-stones-1/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'gameOfStones' function below.
The function is expected to return a STRING.
The function accepts INTEGER n as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/game-of-stones-1/problem
"""

def gameOfStones(n):
    # LWWWWWL LWWWWWL ... this is the pattern
    magic_pattern = 7
    if n == 1 or n % magic_pattern<2:
        return "Second"
    return "First"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        fptr.write(result + '\n')
    fptr.close()

