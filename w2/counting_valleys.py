def counting_valleys(steps: int, path: str) -> int:
    """
    Given an integer number of steps and a string path of equal length
    composed of characters 'U' (uphill) and 'D' (downhill), determine
    how many valleys the hiker traverses. A valley is defined as any
    sequence of consecutive steps that begins with a step down from
    sea level and ends with a step up returning to sea level.

    Parameters:
        steps (int): Total number of steps taken, equals length of path.
        path (str): Sequence of 'U' and 'D' characters describing the hike.

    Returns:
        int: Number of valleys traversed.

    Example:
        >>> counting_valleys(8, "UDDDUDUU")
        1
        >>> counting_valleys(10, "UDUDUDUDUD")
        0
    """
    heights = [0]
    path = list(path)
    height = 0
    for i in range(len(path)):
        if path[i] == 'D':
            height -= 1
        elif path[i] == 'U':
            height += 1
        heights.append(height)
    valleys = 0
    for j in range(len(heights)-1):
        if heights[j] == 0 and heights[j+1] == -1:
            valleys += 1
    return valleys
    
        