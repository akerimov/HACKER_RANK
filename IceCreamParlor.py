#!/usr/bin/env python
# coding: utf-8

"""
Two friends like to pool their money and go to the ice cream parlor. 
They always choose two distinct flavors and they spend all of their money.
Given a list of prices for the flavors of ice cream, select the two that 
will cost all of the money they have.

Function Description:
Complete the icecreamParlor function below.
icecreamParlor has the following parameters:
INPUT:
    int m: the amount of money they have to spend
    int cost[n]: the cost of each flavor of ice cream
OUTPUT:
    int[2]: the indices of the prices of the two flavors they buy, sorted ascending
    
Link to problem statement: 
https://www.hackerrank.com/challenges/icecream-parlor/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

"""
Complete the 'icecreamParlor' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts following parameters:
  1. INTEGER m
  2. INTEGER_ARRAY arr
  
Link to problem statement: 
https://www.hackerrank.com/challenges/icecream-parlor/problem
"""

def icecreamParlor(budget, cost):
    for item in itertools.combinations(range(0, len(cost)),2):
        if (cost[item[0]] + cost[item[1]]) == budget:
            return [item[0]+1, item[1]+1]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        budget = int(input().strip())
        n = int(input().strip())
        cost = list(map(int, input().rstrip().split()))
        result = icecreamParlor(budget,cost)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()
