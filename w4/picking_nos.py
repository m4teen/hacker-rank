def pickingNumbers(a):
    """
    Given a list of integers `a`, return the length of the largest multiset
    (subset, ignoring order) where the absolute difference between any two
    elements is at most 1.

    The function works by iterating over each distinct integer value in `a`,
    counting its occurrences, and pairing it with occurrences of either the
    value immediately below or above (if present), choosing the larger sum.
    Returns 0 if `a` is empty.
    
    Parameters:
        a (List[int]): Input list of integers.

    Returns:
        int: Maximum size of a valid subset where max difference ≤ 1.
    """
    b = sorted(set(a))
    candidates = []
    for i in range(len(b)):
        candidate = [b[i]]*(a.count(b[i]))
        if i != 0 and (b[i]-1) in a:
            candidate.extend([b[i-1]]*(a.count(b[i-1])))
        elif i != (len(b)-1) and i!=0 and (b[i] + 1) in a:
            candidate.extend([b[i+1]]*(a.count(b[i+1])))            
        candidates.append(candidate)
    if len(candidates) != 0: 
            return  max([len(candidates[i]) for i in range(len(candidates))])
    else:
        return 0  


