#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
You wish to buy video games from the famous online video game store Mist.
Usually, all games are sold at the same price, p dollars. However, they are planning to have the seasonal 
Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game will 
cost p dollars, and every subsequent game will cost  d dollars less than the previous one. This continues 
until the cost becomes less than or equal to m dollars, after which every game will cost  dollars. How many 
games can you buy during the Halloween Sale?

Function Description
Complete the howManyGames function below.
howManyGames has the following parameters:
INPUT: 
    int p: the price of the first game
    int d: the discount from the previous game price
    int m: the minimum cost of a game
    int s: the starting budget
RETURN:
    int number of bought games
    
Link to problem statement:
https://www.hackerrank.com/challenges/halloween-sale/problem?isFullScreen=true
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'howManyGames' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s

def howManyGames(p, d, m, s):
    
    # initialize number of games
    count = 0 
    
    # loop until budget is enough 
    while s>=m:
        
        # check if the current budget is less than the game price
        if s<p:
            return count 
        
        # check if game prices is less than the minimum price
        if p < m:
            # update the game price to minimum price
            p = m
        # update the budget
        s = s - p
        # update the budget, apply discount
        p = p - d
        # update the number of games
        count +=1 
    
    return count 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    p = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    m = int(first_multiple_input[2])
    s = int(first_multiple_input[3])
    answer = howManyGames(p, d, m, s)
    fptr.write(str(answer) + '\n')
    fptr.close()

