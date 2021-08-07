#!/usr/bin/env python
# coding: utf-8

"""
Jim's Burgers has a line of hungry customers. Orders vary in the time it takes to prepare them. 
Determine the order the customers receive their orders. Start by numbering each of the customers 
from 1 to n, front of the line to the back. You will then be given an order number and a preparation 
time for each customer.  The time of delivery is calculated as the sum of the order number and the 
preparation time. If two orders are delivered at the same time, assume they are delivered in ascending 
customer number order.

Function Description:
Complete the jimOrders function below. It should return an array of integers that represent the order 
that customers' orders are delivered.

jimOrders has the following parameter:
INPUT:
    orders: a 2D integer array where each orders[i] is in the form [order[i],prep[i]].
OUTPUT:
    Print a single line of n space-separated customer numbers that describes the sequence 
    in which the customers receive their burgers. If two or more customers receive their 
    burgers at the same time, print their numbers in ascending order

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
Complete the 'jimOrders' function below.
The function is expected to return an INTEGER_ARRAY.
The function accepts 2D_INTEGER_ARRAY orders as parameter.

Link to problem statement:
https://www.hackerrank.com/challenges/jim-and-the-orders/problem
"""

def jimOrders(orders): 
    # create the delivery dictionary
    # key= customer number, value = delivery time
    delivery = {}
    
    # loop over each order 
    for index in range(len(orders)):
        # number each of the customers from  1 
        customer= index + 1
        # add delivery time to dictionary 
        delivery[customer] = sum(orders[index])
    
    # sort delivery dictionary by value = delivery time  
    sort_delivery = dict(sorted(delivery.items(), key = lambda item: item[1]))
    
    # return the the keys = customer numbers
    return sort_delivery.keys()

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    orders = []
    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))
    result = jimOrders(orders)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
