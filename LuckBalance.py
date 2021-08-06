#!/usr/bin/env python
# coding: utf-8

"""
Lena is preparing for an important coding competition that is preceded by a number of sequential 
preliminary contests. Initially, her luck balance is 0. She believes in "saving luck", and wants 
to check her theory. Each contest is described by two integers, L[i] and T[i]:
    - L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance 
      will decrease by L[i]; if she loses it, her luck balance will increase by L[i].
    - T[i]denotes the contest's importance rating. It's equal to 1 if the contest is important, 
      and it's equal to 0 if it's unimportant.
If Lena loses no more than k important contests, what is the maximum amount of luck she can have after 
competing in all the preliminary contests? This value may be negative.

Function Description:
Complete the luckBalance function below.
luckBalance has the following parameter:
INPUT:
    int k: the number of important contests Lena can lose
    int contests[n][2]: a 2D array of integers where each contest[i] contains two integers that 
    represent the luck balance and importance of the ith contest

Link to problem statement: 
https://www.hackerrank.com/challenges/luck-balance/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'luckBalance' function below.
The function is expected to return an INTEGER.
The function accepts following parameters:
  1. INTEGER k
  2. 2D_INTEGER_ARRAY contests

Link to problem statement: 
https://www.hackerrank.com/challenges/luck-balance/problem
"""

def luckBalance(k, contests):
    important = []
    not_important = []
    # separate the important from not important ratings 
    for item in contests:
        if item[1] == 1:
            important.append(item[0])
        else:
            not_important.append(item[0]) 
    
            # total luck balance if k is greater than number of important ratings
    luck_balance = sum(important) + sum(not_important)
    # check if k is less than number of important ratings
    if k < len(important):
        # update the luck balance (substract the losses)
        luck_balance -= 2*sum(sorted(important, reverse=True)[k:])
    
    return luck_balance
        
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')
    fptr.close()
