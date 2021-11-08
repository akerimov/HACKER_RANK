#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
A group of friends want to buy a bouquet of flowers. The florist wants to maximize his number of new customers and the money he makes. 
To do this, he decides he'll multiply the price of each flower by the number of that customer's previously purchased flowers plus 1. 
The first flower will be original price, (0+1)*original_price, the next will be (1+1)*original_price and so on.

Given the size of the group of friends, the number of flowers they want to purchase and the original prices of the flowers, 
determine the minimum cost to purchase all of the flowers. The number of flowers they want equals the length of the  array.

Function Description
Complete the getMinimumCost function below.
getMinimumCost has the following parameter(s):
INPUT:
    int c[n]: the original price of each flower
    int k: the number of friends
RETURN
    int: the minimum cost to purchase all flowers

Link to problem statement:
https://www.hackerrank.com/challenges/greedy-florist/problem?isFullScreen=true
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    # initialize the minimum cost for the bouquet of flowers
    minimum_cost = 0

    # check if number of friends vs. number of flowers
    if k == len(c):
        # each friend buys exactly one flower 
        minimum_cost = sum(c)
    else:
        
        # sort the array of original price of each flower 
        c = sorted(c, reverse=True)
        # inialize the number of flowers boughts by each customer
        flower_count_per_customer = 0
        # loop over the index in flower price array 
        for index in range(0,len(c),k):
            # multiply the price of each flower by the number of that customer's previously purchased flowers plus 1.
            if (len(c) - 1 -(index)) < k:
                minimum_cost += sum(c[index:])*(flower_count_per_customer+1)
            else: 
                minimum_cost += sum(c[index:index+k])*(flower_count_per_customer+1)
            flower_count_per_customer += 1             
    return minimum_cost
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    fptr.write(str(minimumCost) + '\n')
    fptr.close()

