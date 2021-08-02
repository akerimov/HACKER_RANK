#!/usr/bin/env python
# coding: utf-8

"""
Given a sorted list with an unsorted number  in the rightmost cell, can you write some simple 
code to insert  into the array so that it remains sorted? Since this is a learning exercise, 
it won't be the most efficient way of performing the insertion. It will instead demonstrate 
the brute-force method in detail.

Assume you are given the array arr=[1,2,4,5,3] indexed 0 ... 4. Store the value of arr[4]. 
Now test lower index values successively from 3 to 0 until you reach a value that is lower 
than arr[4] at arr[1]  in this case. Each time your test fails, copy the value at the lower
index to the current index and print your array. When the next lower indexed value is smaller 
than arr[4], insert the stored value at the current index and print the entire array.

Complete the insertionSort1 function below.
insertionSort1 has the following parameter:
INPUT:
    n: an integer, the size of 
    arr: an array of integers to sort
OUTPUT:
    Print the interim and final arrays, each on a new line. No return value is expected.
    
Link to problem statement:
https://www.hackerrank.com/challenges/insertionsort1/problem
"""

#!/bin/python3
import math
import os
import random
import re
import sys

"""
Complete the 'insertionSort1' function below.
The function accepts following parameters:
  1. INTEGER n
  2. INTEGER_ARRAY arr
  
Link to problem statement:
https://www.hackerrank.com/challenges/insertionsort1/problem
"""

def insertionSort1(n, arr):
    # store the last item as last_num
    last_num = arr[-1]
    
    # start looping over the index at n-1
    # stop at index 1
    for index in range(n-1, 0,-1):
        if index == 0:
            #update the current item with last_num
            arr[index] = last_num
            # print current array
            print(*arr)
        # check if next item is greater than last_num
        elif arr[index-1] > last_num:
            #update the current item with next item  
            arr[index] = arr[index-1]
            # print current array
            print(*arr)
        else:
            #update the current item with last_num
            arr[index] = last_num
             # print current array
            print(*arr)
            break
    
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort1(n, arr)

