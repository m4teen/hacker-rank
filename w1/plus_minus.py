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
    """
    Given an array of integers, calculate the ratios of its positive, negative, and zero elements.
    Print the decimal value of each fraction on a new line with exactly 6 decimal places.

    The function should not return a value.

    Function Signature:
        plusMinus(arr: list[int]) -> None

    Parameters:
        arr (list[int]): An array of integers.

    Task:
        - Calculate the ratio of positive elements in the array.
        - Calculate the ratio of negative elements in the array.
        - Calculate the ratio of zeros in the array.
        - Print each ratio on a new line with 6 digits after the decimal point.

    Constraints:
        0 < n ≤ 100
        -100 ≤ arr[i] ≤ 100

    Input Format:
        - The first line contains an integer n, the size of the array.
        - The second line contains n space-separated integers, the elements of arr.

    Output Format:
        - Three lines, each containing a ratio with exactly 6 decimal places:
            1. Proportion of positive values.
            2. Proportion of negative values.
            3. Proportion of zeros.

    Example:
        Input:
            6
            -4 3 -9 0 4 1
        Output:
            0.500000
            0.333333
            0.166667

    Explanation:
        There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
        The ratios are:
            Positive: 3/6 = 0.500000
            Negative: 2/6 = 0.333333
            Zero:     1/6 = 0.166667
    """

    pos = 0
    neg = 0
    zer = 0
    for n in arr:
        if n == 0:
            zer += 1
        elif n >0:
            pos += 1
        else:
            neg += 1
    
    print(f'{pos/len(arr):.6f}')
    print(f'{neg/len(arr):.6f}')
    print(f'{zer/len(arr):.6f}')




if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
