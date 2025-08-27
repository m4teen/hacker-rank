def diagonal_difference(arr):
    """
    Compute the absolute difference between the sums of the two diagonals of a square matrix.

    Given `arr`, a 2-D square array of integers of size n×n, this function calculates:
      • the sum of the primary diagonal (from top-left to bottom-right): sum(arr[i][i] for i in range(n))
      • the sum of the secondary diagonal (from top-right to bottom-left): sum(arr[i][n-1-i] for i in range(n))
    It returns the absolute difference between these two sums.

    Parameters:
        arr (List[List[int]]): a square matrix of integers (n rows by n columns)

    Returns:
        int: the absolute difference between the sums of the primary and secondary diagonals

    Example:
        For the matrix
            11  2   4
             4  5   6
            10  8 –12
        primary sum = 11 + 5 − 12 = 4
        secondary sum =  4 + 5 + 10 = 19
        returned value = |4 − 19| = 15
    """
    d1 = sum(arr[i][i] for i in range(len(arr)))
    d2 = sum(arr[i][len(arr)-1-i] for i in range(len(arr)))
    
    return abs(d1-d2)