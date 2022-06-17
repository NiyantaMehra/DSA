#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
    # Write your code here
    binary = "{:032b}".format(n)
    # binary = binary[2:]
    reverse = binary.replace('0','#') 
    reverse = reverse.replace('1','0') 
    reverse = reverse.replace('#','1')   
    return (int(reverse,2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
