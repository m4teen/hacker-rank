def strings_xor(s, t):
    """
    Compute the bitwise XOR of two binary strings of equal length.

    Given two strings s and t composed exclusively of '0' and '1' characters
    and sharing identical length, return a new string such that each character
    is the XOR of the corresponding characters in s and t:
    '1' if exactly one of the characters is '1', otherwise '0'.

    Constraints:
        - len(s) == len(t)
        - s and t contain only '0' or '1'

    Parameters:
        s (str): First binary string.
        t (str): Second binary string.

    Returns:
        str: Resulting binary string after XOR.

    Example:
        >>> strings_xor("10101", "00101")
        '10000'

        Because:
        1 XOR 0 = 1
        0 XOR 0 = 0
        1 XOR 1 = 0
        0 XOR 0 = 0
        1 XOR 1 = 0
    """
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0'
        else:
            res += '1'

    return res

