#!/bin/python3
#https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
import math
import os
import random
import re
import sys
from collections import defaultdict

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, S):
    # Write your code here

    mods = [item % k for item in S]
    freqs = defaultdict(int)
    for elem in mods:
        freqs[elem] += 1
    total = 0
    for key, val in freqs.items():
        if val == 0:
            continue
        if key == 0:
            total += 1
        elif (k - key) == key:
            total += 1
        elif key > (k - key):
            if (k - key) in freqs:
                total +=  max([val, freqs[k - key]])
            else:
                total += val
        elif key < (k - key):
            if (k - key not in freqs):
                total += val
    return total

     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
