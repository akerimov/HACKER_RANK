#!/usr/bin/env python
# coding: utf-8

"""
There is a collection of rocks where each rock has various minerals embeded in it. 
Each type of mineral is designated by a lowercase letter. There may be multiple 
occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs 
at least once in each of the rocks in the collection. 

Given a list of minerals embedded in each of the rocks, display the number of types 
of gemstones in the collection.

Function Description:
Complete the gemstones function below.
gemstones has the following parameter:
INPUT:
    string arr[n]: an array of strings
OUTPUT:
    int: the number of gemstones found
    
Link to problem statement:
https://www.hackerrank.com/challenges/separate-the-numbers/problem
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

"""
Complete the 'gemstones' function below.
The function is expected to return an INTEGER.
The function accepts STRING_ARRAY arr as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/gem-stones/problem
"""

def gemstones(arr):
    gemstones = 0 
    mydict = {}
    for rock in arr:
        for ch in set(rock):
            if ch in mydict:
                mydict[ch] +=1
            else:
                mydict[ch] = 1
    print(mydict)
    
    for key in mydict:
        if mydict[key] == len(arr):
            gemstones +=1
    return gemstones
        
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    n = int(input().strip())
#    arr = []
#    for _ in range(n):
#        arr_item = input()
#        arr.append(arr_item)
#    result = gemstones(arr)
#    fptr.write(str(result) + '\n')
#    fptr.close()
