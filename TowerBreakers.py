#!/usr/bin/env python
# coding: utf-8

"""
Two players are playing a game of Tower Breakers! Player 1 always moves first, 
and both players always play optimally.The rules of the game are as follows:
    (1) Initially there are n towers.
    (2) Each tower is of height m.
    (3) The players move in alternating turns.
    (4) In each turn, a player can choose a tower of height x and reduce its height to y, 
        where 1<=y<x and y evenly divides x.
    (5) If the current player is unable to make a move, they lose the game.

Given the values of m and n, determine which player will win. 
If the first player wins, return 1. Otherwise, return 2.
      
Link to problem statement:
https://www.hackerrank.com/challenges/tower-breakers-1/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'towerBreakers' function below.
The function is expected to return an INTEGER.
The function accepts following parameters:
  1. INTEGER n
  2. INTEGER m

Link to problem statement: 
https://www.hackerrank.com/challenges/tower-breakers-1/problem
"""

def towerBreakers(n, m):
    if n%2 == 0 or m==1:
        return 2
    return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = towerBreakers(n, m)
        fptr.write(str(result) + '\n')
    fptr.close()
