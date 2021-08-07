#!/usr/bin/env python
# coding: utf-8

"""
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row 
alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, 
top to bottom. Return YES if they are or NO if they are not.

Function Description:
Complete the gridChallenge function below.

gridChallenge has the following parameter(s):
INPUT:
    string grid[n]: an array of strings
OUTPUT:
    string: either YES or NO

Link to problem statement:
https://www.hackerrank.com/challenges/jim-and-the-orders/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'gridChallenge' function below.
The function is expected to return a STRING.
The function accepts STRING_ARRAY grid as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/grid-challenge/problem
"""

def gridChallenge(grid):
    # loop over each row in grid
    for row in range(len(grid)):
        # sort row in ascending order
        grid[row] = sorted(grid[row])
    
    # loop over each column in grid
    for col in range(len(grid[0])):
        # initialize column vector
        column = []
        # loop over each row in grid
        for row in range(len(grid)):
            # update the column vector
            column.append(grid[row][col])
        # check if column is sorted in ascending order
        if column != sorted(column):
            return "NO"
    return "YES"
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        grid = []
        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)
        result = gridChallenge(grid)
        fptr.write(result + '\n')
    fptr.close()
