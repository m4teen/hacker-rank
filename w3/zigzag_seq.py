def find_zig_zag_sequence(a, n):
    """
    Given a list of distinct integers of odd length, permute it into the lexicographically
    smallest zig-zag sequence.

    A zig-zag sequence is one in which the first (n+1)/2 elements ascend (strictly increasing),
    and the remaining (n-1)/2 elements descend (strictly decreasing).

    Parameters:
        arr (list[int]): List of distinct integers of odd length n.

    Returns:
        list[int]: The lexicographically smallest zig-zag permutation of the input array.

    Example:
        >>> find_zig_zag_sequence([2, 3, 5, 1, 4])
        [1, 2, 5, 4, 3]
        Explanation:
        - When sorted, array becomes [1, 2, 3, 4, 5].
        - Form zig-zag by keeping first (n+1)//2 = 3 elements in increasing order: [1, 2, 5],
          then the remaining in strictly decreasing order: [4, 3], yielding [1, 2, 5, 4, 3].

    Note:
        - The input length n is guaranteed to be odd.
    """
    a.sort()
    mid = int((n - 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return