#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
A weighted string is a string of lowercase English letters where each letter has a weight. 
Character weights are 1 to 26  from  a to z. The weight of a string is the sum of the weights 
of its characters. A uniform string consists of a single character repeated zero or more times. 
For example, ccc and a are uniform strings, but bcb and cd are not. Given a string, s, let U be 
the set of weights for all possible uniform contiguous substrings of string. There will be  q 
queries to answer where each query consists of a single integer. Create a return array where 
for each query, the value is Yes if q exist in U . Otherwise, append No.
    
Link to problem statement: 
https://www.hackerrank.com/challenges/weighted-uniform-string/problem
"""


# In[ ]:


#!/bin/python3

import math
import os
import random
import re
import sys

"""
Complete the 'weightedUniformStrings' function below.
The function is expected to return a STRING_ARRAY.
The function accepts following parameters:
  1. STRING s
  2. INTEGER_ARRAY queries
  
Link to problem statement: 
https://www.hackerrank.com/challenges/weighted-uniform-string/problem
"""

def weightedUniformStrings(s, queries):
    
    # initialize the sets of weights
    weights_set = set()
    weight =  ord(s[0]) - ((ord('a')-1))
    weights_set.add(weight)
    
    # find the weights for each uniform string
    for index in range(1, len(s)):   
        if s[index-1] == s[index]:
            weight += ord(s[index]) - ((ord('a')-1))
        else:
            weight = ord(s[index]) - ((ord('a')-1))
        weights_set.add(weight)
    #print(weights)
    
    # check if each of queries exist in weights 
    queries_answer = ["Yes" if q in weights_set else "No" for q in queries]
    
    return queries_answer
                
            
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    s = input()
#    queries_count = int(input().strip())
#    queries = []
#
#    for _ in range(queries_count):
#        queries_item = int(input().strip())
#        queries.append(queries_item)
#    result = weightedUniformStrings(s, queries)
#    
#   fptr.write('\n'.join(result))
#   fptr.write('\n')
#    fptr.close()

