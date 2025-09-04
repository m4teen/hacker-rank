def twoArrays(k, A, B):
    """
    Determine whether two integer arrays, A and B, can be permuted into A' and B'
    such that, for every index i, A'[i] + B'[i] ≥ k.

    Parameters:
        k (int): Threshold sum that each paired element must meet or exceed.
        A (list[int]): First array of integers of length n.
        B (list[int]): Second array of integers of length n.

    Returns:
        str: 'YES' if a valid permutation exists; otherwise 'NO'.

    Behaviour:
        Evaluate q independent queries (not shown here). For each, read n and k,
        followed by arrays A and B. If there exists any permutation A', B' such that
        A'[i] + B'[i] ≥ k for all i in [0, n), return 'YES'. Otherwise, return 'NO'.

    Example:
        Given k = 10, A = [2, 1, 3], B = [7, 8, 9]:
        One valid pairing is A' = [3, 2, 1], B' = [7, 8, 9], yielding sums [10, 10, 10].
        The function should return 'YES'.

        Given k = 5, A = [1, 2, 2, 1], B = [3, 3, 3, 4]:
        No permutation exists that satisfies each pair summing to at least 5.
        The function should return 'NO'.
    """
    A = sorted(A)
    B = sorted(B,reverse =True)
    h = 'YES'
    for i in range(len(A)):
        x = A[i]+B[i]
        
        if x >= k:
            continue 
        else:  
            h = 'NO'
            break
    
    
    return h