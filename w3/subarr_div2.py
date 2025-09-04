def birthday(s, d, m):
    """
    Count the number of contiguous segments of length m in the list s
    whose elements sum to exactly d.

    Parameters:
        s (list[int]): A list of integers representing the chocolate squares.
        d (int): The birth day—desired sum of the segment.
        m (int): The birth month—required length of the segment.

    Returns:
        int: The number of valid segments (ways to share the chocolate bar).

    Example:
        >>> birthday([2, 2, 1, 3, 2], 4, 2)
        2
        (Segments [2, 2] at positions 0–1, and [1, 3] at positions 2–3.)

        >>> birthday([1, 1, 1, 1, 1, 1], 3, 2)
        0
        (No contiguous segment of length 2 sums to 3.)
    """
    candidates = 0
    for i in range(len(s)-m+1):
        x = s[i:i+m]
        
        if sum(x) == d:
            candidates += 1
        else:
            continue
    return candidates