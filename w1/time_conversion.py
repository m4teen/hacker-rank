import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    """
    Converts a given time in 12-hour AM/PM format to its equivalent in 24-hour (military) time.

    Notes:
        - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
        - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

    Function Signature:
        def timeConversion(s: str) -> str

    Args:
        s (str): A time in 12-hour clock format (hh:mm:ssAM or hh:mm:ssPM).

    Returns:
        str: The time in 24-hour clock format (HH:MM:SS).

    Constraints:
        - All input times are valid.

    Example:
        Input:  "12:01:00PM"
        Output: "12:01:00"

        Input:  "12:01:00AM"
        Output: "00:01:00"

    Sample Input:
        "07:05:45PM"

    Sample Output:
        "19:05:45"
    """

    t = s.replace(':','')
    time_mil = None

    if t[6:] == 'PM':
        t = t.replace('PM','')
        hr = int(t[0:2])
        if hr == 12:
            hr_mil = 12
            hr_mil_right = f'{hr_mil:02}'
            time_mil_list = list([hr_mil_right, t[2:4], t[4:]])
            time_mil = ':'.join(time_mil_list)
        else:
            hr_mil = (hr + 12) % 24
            hr_mil_right = f'{hr_mil:02}'
            time_mil_list = list([hr_mil_right, t[2:4], t[4:]])
            time_mil = ':'.join(time_mil_list)
    if t[6:] == 'AM':
        t=t.replace('AM','')
        hr = int(t[0:2])

        if hr == 12:
            hr_mil = 00
            hr_mil_right = f'{hr_mil:02}'
            time_mil_list = list([hr_mil_right, t[2:4], t[4:]])
            time_mil = ':'.join(time_mil_list)
        else:
            hr_mil = hr
            hr_mil_right = f'{hr_mil:02}'
            time_mil_list = list([hr_mil_right, t[2:4], t[4:]])
            time_mil = ':'.join(time_mil_list)

    return time_mil
