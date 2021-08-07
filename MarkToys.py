#!/usr/bin/env python
# coding: utf-8

"""
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. 
There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain 
amount to spend, and he wants to maximize the number of toys he buys with this money. Given a list of toy 
prices and an amount to spend, determine the maximum number of gifts he can buy.

Note Each toy can be purchased only once.

Function Description:
Complete the function maximumToys below.
maximumToys has the following parameter(s):
INPUT:
    int prices[n]: the toy prices
    int k: Mark's budget
OUTPUT:
    int: the maximum number of toys

Link to problem statement:
https://www.hackerrank.com/challenges/mark-and-toys/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'maximumToys' function below.\
The function is expected to return an INTEGER.
The function accepts following parameters:
  1. INTEGER_ARRAY prices
  2. INTEGER k

Link to problem statement:
https://www.hackerrank.com/challenges/mark-and-toys/problem
"""

def maximumToys(prices, k):
    prices = sorted(prices)
    index = 0
    total_cost = 0
    while total_cost < k:
        print("TOTAL COST: ", total_cost)
        total_cost += prices[index]
        index +=1
    return index-1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()
