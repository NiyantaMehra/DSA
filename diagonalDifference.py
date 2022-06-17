#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    m = len(arr[0])
    sum_1 = 0
    sum_2 = 0
    for i in range(n):
        for j in range(m):
            #main diagonal
            if i==j:
                sum_1 = sum_1 + arr[i][j]
            #opposite diagonal
            if j == n - i - 1:
                sum_2 = sum_2 + arr[i][j]
    return abs(sum_1-sum_2)            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
