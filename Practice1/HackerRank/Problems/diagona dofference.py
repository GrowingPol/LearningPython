#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, n):
    diagonal_lr = [] * n
    diagonal_rl = [] * n
    count = 0
    for row in range(n):
        print(row)
        diagonal_lr.append(arr[row][row])

    for row in range(n-1, -1, -1):
        diagonal_rl.append(arr[row][count])
        count += 1

    print(f'rl {diagonal_rl} lr {diagonal_lr}')
    return abs(sum(diagonal_lr) - sum(diagonal_rl))


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)
    result = diagonalDifference(arr, n)

    print(str(result) + '\n')