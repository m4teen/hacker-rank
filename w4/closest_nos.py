def closestNumbers(arr):
    """
    From an unsorted list of unique integers, find all pairs with the smallest absolute difference.
    Return their elements in ascending order, flattened.

    Parameters:
        arr (list of int): input list, all values are unique

    Returns:
        list of int: flattened list of all pairs (a, b) such that |a - b| is minimal among all pairs.
                     Each pair (a, b) appears in sorted order (a < b), and pairs are output in ascending
                     order by first element, then second.

    Description:
        Approach:
            - Sort the array: any minimal-difference pair must be adjacent.
            - Compute differences between each adjacent pair.
            - Identify the minimal difference.
            - Collect all adjacent pairs matching that difference, in order.
            - Flatten result: [(a1, b1), (a2, b2), ...] → [a1, b1, a2, b2, ...].

        Examples:
            Input: [5, 4, 3, 2] → sorted [2, 3, 4, 5]
            Differences: 1, 1, 1 → minimal = 1
            Pairs: (2, 3), (3, 4), (4, 5)
            Return: [2, 3, 3, 4, 4, 5]

            Input: [-20, 30, ...] where -20 and 30 are closest → Return: [-20, 30]
    """
    n = len(arr)
    arr = sorted(arr)
    candidates = []
    for i in range(0, n-1):
        candidates.append(arr[i+1] - arr[i])
    
    minimum = min(candidates)
    
    an = [(arr[i], arr[i+1]) for i in range(0, n-1) if arr[i+1] - arr[i] == minimum]
    answer = [item for tup in an for item in tup]
    return answer
