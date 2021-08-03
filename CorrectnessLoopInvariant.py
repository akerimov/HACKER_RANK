#!/usr/bin/env python
# coding: utf-8

"""
Challenge
In the InsertionSort code below, there is an error. Can you fix it? Print the array only once, when it is fully sorted.
Input Format
There will be two lines of input:
 - n, the size of the array
 - arr, the list of numbers that makes up the array
    
Link to problem statement:
https://www.hackerrank.com/challenges/correctness-invariant/problem
"""

#!/bin/python3
"""
Complete the 'insertion_sort' function below.
The function accepts following parameters:
    1. INTEGER n
    2. INTEGER_ARRAY arr
    
Link to problem statement:
https://www.hackerrank.com/challenges/correctness-invariant/problem
"""

def insertion_sort(n, arr):
    # loop over the elements in the unsorted array
    for i in range(1, n):
        # store the element as a key and compare with elements to its left
        j = i-1
        key = arr[i]
        # loop over the elements to key's left 
        # check if they are greater than the key element
        while (j >= 0) and (arr[j] > key):
            # update the element to its right with current element
            arr[j+1] = arr[j]
            # update the current index 
            j -= 1
        # update the element to its right with key element
        arr[j+1] = key
        
if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    insertion_sort(n, arr)
    print(" ".join(map(str,arr)))
