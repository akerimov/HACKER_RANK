#!/usr/bin/env python
# coding: utf-8

"""
A child is playing a cloud hopping game. In this game, there are sequentially 
numbered clouds that can be thunderheads or cumulus clouds. The character must 
jump from cloud to cloud until it reaches the start again.

There is an array of clouds, c and an energy level e=100. The character starts 
from c[0] and uses -1 unit of energy to make a jump of size k to cloud c[(i+k)%n].
If it lands on a thundercloud, c[i]=1, its energy (e) decreases by 2 additional units. 
The game ends when the character lands back on cloud 0.

Given the values of k and the configuration of the clouds as an array c, 
determine the final value of e after the game ends.

Function Description
Complete the jumpingOnClouds function below.
jumpingOnClouds has the following parameter(s):
INPUT:
    int c[n]: the cloud types along the path
    int k: the length of one jump
OUTPUT:
    int: the energy level remaining.

Link to problem statement:
https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    # initialize energy 
    energy = 100
    # first cloud jump 
    index = (0+k) % len(c)  
    # energy after first cloud jump
    energy = energy - 1 - 2*c[index] 
    
    # game ends when the character lands back on cloud 0
    while index != 0:
        # update cloud jump
        index = (index+k) % len(c)
        # update energy after jump
        energy = energy - 1 - 2*c[index]
    return energy    
              
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    fptr.write(str(result) + '\n')
    fptr.close()
