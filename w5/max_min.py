def maxMin(k, arr):
    """
    Compute the minimum “unfairness” among all ways to select k elements from arr.

    Unfairness is defined as the difference between the largest and smallest element in a selected subset of size k.

    Parameters:
        k (int): The number of elements to choose.
        arr (List[int]): The list of integers from which subsets are drawn.

    Returns:
        int or float: The minimum unfairness, i.e. the smallest possible (max − min)
                       among all subsets of size k in arr.

    Preconditions:
        - 1 ≤ k ≤ len(arr).
        - Elements of arr are comparable (integers in this case).
        - arr may contain duplicates.
    """
    n = len(arr)
    arr.sort()
    candidate = float('inf')
    for i in range(len(arr)):
        if i+k <= n:
            unfairness = arr[i+k-1] - arr[i]
            if unfairness < candidate:
                candidate = unfairness
        else:
            continue
    return candidate

