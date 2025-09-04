def sockMerchant(n, ar):
    """
    Count the number of matching sock pairs in a pile.

    Given a total count of socks and their colours, determine how many
    pairs of the same colour can be formed. Each sock may be used
    in at most one pair.

    Parameters:
        n (int): Number of socks in the pile.
        ar (list[int]): List of integers representing sock colours.

    Returns:
        int: Total number of matching pairs.

    Example:
        >>> sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
        3
        (Pairs: two of colour 10, one of colour 20.)
    """
    grand_total = 0
    unique_els = list(set(ar))
            
    for i in range(len(unique_els)):
        y = ar.count(unique_els[i])
            
        ind_pairs_total = y//2
        grand_total += ind_pairs_total
    
    return grand_total