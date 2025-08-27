def countingSort(arr):
    """
    Compute the frequency distribution of values in the range 0–99.

    Given `arr`, a list of non-negative integers, return a list of length 100
    where each index `i` indicates the count of `i` in the input list.

    Behaviour:
      • Always returns an integer list of length 100.
      • For each `val` in `arr`, increment the count at index `val`.
      • Values are assumed to lie within the inclusive range 0 to 99.

    Parameters:
        arr (List[int]): List of integers, each satisfying 0 ≤ val < 100.

    Returns:
        List[int]: A 100-element list where the value at index i is the
                   frequency of i in `arr`.

    Example:
        Input: arr = [63, 25, 73, 1, 63]
        Frequency array (first few entries):
          index 0: 0
                1: 1
               ...
               25: 1
               ...
               63: 2
               ...
               73: 1
               rest: 0
    """
    ind = [0] * 100

    for val in arr:
        ind[val] += 1

    return ind
