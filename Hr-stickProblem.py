import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # # Write your code here
    # arr_length = len(arr)
    # smallest_number = min(arr)
    # asx = []
    # asx.append[len(arr)]
    # # for x in arr:
    # #     arr[x] = arr[x]-smallest_number
    
    # for i in range(1,len(arr)):
    #     arr[i]= arr[i]-smallest_number
    #     asx.append[arr[i]]
        
    # return asx[]
    
    # print(len(arr))
    # while True:                 
    #     arr = [x for x in arr if x != min(arr)] 
    #     if len(arr)==0:
    #         break
    #     print(len(arr))
    
    out = []
    while arr:
        out.append(len(arr))
        m = min(arr)
        arr = [x - m for x in arr if x > m]
    return out
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
