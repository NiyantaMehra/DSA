#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0.0
    neg = 0.0
    zero = 0.0
    
    for i in range(0,len(arr)):
        if arr[i] == 0:
            zero = zero + 1.0
        if arr[i] > 0:
            pos = pos + 1.0
        if arr[i] < 0:
            neg = neg + 1.0
    pos = pos/len(arr)
    neg = neg/len(arr)
    zero = zero/len(arr)
    pos_new = "{:.6f}".format(pos)
    print(pos_new)
    neg_new = "{:.6f}".format(neg)
    print(neg_new)
    zero_new = "{:.6f}".format(zero)
    print(zero_new)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
