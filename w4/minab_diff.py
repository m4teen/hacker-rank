def minimumAbsoluteDifference(arr):
    """
    Compute the minimum absolute difference between any two elements in the array.

    Given an array of integers, determine the smallest positive difference |a - b|
    for any pair of distinct elements a and b in the array.

    Parameters
    ----------
    arr : List[int]
        A list of integers.

    Returns
    -------
    int
        The minimum absolute difference between any two elements in the list.

    Behaviour
    ---------
    - Sorts the array.
    - Compares only adjacent elements to find the minimum difference.
    - Runs in O(n log n) time due to sorting, and O(n) space (if sorting in place).

    Constraints
    -----------
    - 2 ≤ n ≤ 10^5 (length of arr)
    - Each arr[i] is an integer with value between –10^9 and 10^9

    Input Format (as per HackerRank)
    ----------------------------------
    The first line of input is an integer n, the number of elements in arr.
    The second line contains n space-separated integers representing arr.

    Returns
    -------
    int
        An integer representing the minimum absolute difference found between any two elements.

    Example
    -------
    Input (as separate lines):
        5
        1 -3 71 68 17

    After sorting: [-3, 1, 17, 68, 71]
    Adjacent differences: 4, 16, 51, 3
    Returns: 3
    """
    a = sorted(arr)
    minim = float('inf')
    for j in range(1,len(a)):
        if abs(a[j] - a[j-1]) < minim:
            minim = abs(a[j] - a[j-1])
        else:
            continue
    return minim