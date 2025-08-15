import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    """
    Determine the number of times a player breaks their season records for most and least points scored.

    Maria plays basketball and tracks her performance over a season. Her scores are recorded in order of games played.
    The score from the first game establishes both her minimum and maximum record for the season.
    For each subsequent game:
        - If her score is higher than her current maximum record, she sets a new maximum record.
        - If her score is lower than her current minimum record, she sets a new minimum record.
    This function returns the number of times she breaks each record.

    Parameters
    ----------
    scores : list[int]
        A list of integers representing the points scored per game, in chronological order.

    Returns
    -------
    list[int]
        A two-element list:
        - Index 0: Number of times Maria breaks her record for most points in a game.
        - Index 1: Number of times Maria breaks her record for least points in a game.

    Example
    -------
    >>> breakingRecords([12, 24, 10, 24])
    [1, 1]

    Constraints
    -----------
    1 <= len(scores) <= 1000
    0 <= scores[i] <= 10^8
    """

    max_score = scores[0]
    min_score = scores[0]
    max_broken = 0
    min_broken = 0

    for score in scores:
        if score >= max_score:
            max_score = score
            max_broken += 1
        elif score <= min_score:
            min_score = score
            min_broken +=1
        else:
            continue
    
    return list([max_broken,min_broken])


print(breakingRecords([12,24,10,24]))
