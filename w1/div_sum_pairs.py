def divisibleSumPairs(n, k, arr):
    """
    Count the number of index pairs (i, j) in an array such that:
      - i < j
      - The sum arr[i] + arr[j] is divisible by k.

    Parameters
    ----------
    n : int
        The length of the array `arr`.
    k : int
        The divisor to check for divisibility of pair sums.
    arr : list of int
        List of integers (length `n`), where each value satisfies 1 <= arr[i] <= 100.

    Returns
    -------
    int
        The number of valid pairs (i, j) where i < j and
        (arr[i] + arr[j]) % k == 0.

    Example
    -------
    >>> divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])
    5
    # Valid pairs are:
    # (0, 2) -> 1 + 2 = 3
    # (0, 5) -> 1 + 2 = 3
    # (1, 3) -> 3 + 6 = 9
    # (2, 4) -> 2 + 1 = 3
    # (4, 5) -> 1 + 2 = 3
    """
    number = 0
    
    for i,val in enumerate(arr):
        for j in range(i+1,n): # edge case of the last entry protected against since range(n,n) is empty so the entire for loop is skipped as there is nothing to loop over
            if (val + arr[j]) % k == 0:
                number += 1
            else:
                continue
    
    return number 

print(divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]))