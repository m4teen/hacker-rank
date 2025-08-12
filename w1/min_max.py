import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    """
    Given five positive integers, find the minimum and maximum values that can be calculated 
    by summing exactly four out of the five integers. Print these values as a single line of 
    two space-separated long integers.

    Example:
        arr = [1, 3, 5, 7, 9]
        The minimum sum is 1 + 3 + 5 + 7 = 16
        The maximum sum is 3 + 5 + 7 + 9 = 24
        Output: "16 24"

    Function Description:
        Complete the function miniMaxSum with the following parameter:
            arr (list[int]): A list of 5 positive integers.

        The function prints:
            Two space-separated long integers representing the minimum and maximum sum 
            obtainable by summing exactly four out of the five integers.

    Input Format:
        A single line of five space-separated integers.

    Constraints:
        1 ≤ arr[i] ≤ 10^9

    Output Format:
        Two space-separated long integers: 
            - Minimum sum of four out of five integers
            - Maximum sum of four out of five integers

    Sample Input:
        1 2 3 4 5

    Sample Output:
        10 14

    Explanation:
        For the numbers 1, 2, 3, 4, 5:
            - Exclude 1: sum = 2 + 3 + 4 + 5 = 14
            - Exclude 2: sum = 1 + 3 + 4 + 5 = 13
            - Exclude 3: sum = 1 + 2 + 4 + 5 = 12
            - Exclude 4: sum = 1 + 2 + 3 + 5 = 11
            - Exclude 5: sum = 1 + 2 + 3 + 4 = 10
        Minimum sum = 10, Maximum sum = 14

    Hint:
        Beware of integer overflow. Use 64-bit integers.
    """

    copy1 = arr[:]
    copy1.remove(1)
    y = sum(copy1)

    max_sum = y 
    min_sum = y

    for i in arr:
        copy = arr[:]
        copy.remove(i)
        x= sum(copy)

        if x > max_sum:
            max_sum = x
        elif x < min_sum: 
            min_sum = x
        else:
            continue

    print(min_sum,max_sum)
        


miniMaxSum([1,2,3,4,5])