#!/usr/bin/env python
# coding: utf-8

"""
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
Then, characters are written into a grid, whose rows and columns have the 
following constraints:
    (1) math.floor(L) <= row <= column < math.ceil(L)
    (2) Ensure that rowsxcolumns >= L
    (3) If multiple grids satisfy the above conditions, 
        choose the one with the minimum area, i.e. rows x columns .

Function Description
Complete the encryption function below.
encryption has the following parameter(s):
INPUT:
    string s: a string to encrypt
OUTPUT:
    string: the encrypted string

Link to problem statement:
https://www.hackerrank.com/challenges/encryption/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'encryption' function below.
The function is expected to return a STRING.
The function accepts STRING s as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/encryption/problem
"""

def encryption(text):
    # remove the space from the text
    text_no_space = ("").join(text.split())
    
    # find the rows and columns following the constraints
    rows_num = math.floor(len(text_no_space)**0.5)
    columns_num = math.ceil(len(text_no_space)**0.5)
    
    # ensure that rowsxcolumns >= L
    if rows_num * columns_num < len(text_no_space):
        rows_num +=1
    
    # after removing spaces, write the string in the form of a grid 
    # with number of rows and columns
    grid = []
    col_start = 0
    col_end = columns_num 
    for row  in range(rows_num):
        grid.append(text_no_space[col_start:col_end])
        col_start = col_end
        col_end = col_end + columns_num
    
    # encoded message is obtained by displaying the characters of each column, 
    # with a space between column texts
    encrypted_text = []
    for col in range(columns_num):
        encrypted_word = ''
        for row in range(rows_num):
            if col>= len( grid[row]):
                break 
            encrypted_word += grid[row][col]
        encrypted_text.append(encrypted_word)
    return (" ").join(encrypted_text)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = encryption(s)
    fptr.write(result + '\n')
    fptr.close()
