#!/usr/bin/env python
# coding: utf-8

"""
In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. Using the same approach repeatedly, can you sort an entire array?
Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first 
step, when you consider an array with just the first element, it is already sorted since there's nothing to compare it to. In this challenge, print the array after 
each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element 
is already sorted, begin printing after placing the second element.

Function Description
Complete the insertionSort2 function below.
insertionSort2 has the following parameter:
INPUT:
    int n: the length of 
    int arr[n]: an array of integers
OUPUT:
    print at each iteration, print the array as space-separated integers on its own line.
    
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
Complete the 'insertionSort2' function below.
The function accepts following parameters:
    1. INTEGER n
    2. INTEGER_ARRAY arr
    
Link to problem statement:
https://www.hackerrank.com/challenges/insertionsort2/problem
"""

def insertionSort2(n, arr):
    # loop over the elements in array (from left to right) 
    # in order to place them in the sorted way
    original_index = 1
    while original_index < n:
    
        # store the element to be placed as placement_element
        placement_element = arr[original_index]
        # remove the placement_element from the array 
        arr.pop(original_index)
    
        # loop over the indices (from right to place) 
        # before the the original index of element to be placed  
        current_index = original_index-1
        while current_index>=0:
            # if placement element is greater than the current element
            if placement_element > arr[current_index]:
                # insert the placement element after the current elemement
                arr.insert(current_index+1, placement_element)
                break
        
            # if not placement found at index=0
            if current_index == 0:
                # insert the placement element at index = 0
                arr.insert(current_index, placement_element)
            
            # update the current index (from right to left)
            current_index -= 1
        
        #update the original index of placement elemens (from left to right)
        original_index +=1
    
        #print updated array
        print(*arr)

    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort2(n, arr)
