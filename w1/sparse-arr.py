def matchingStrings(strings, queries):
    """
    Count the frequency of each query string in a list of input strings.

    For each query string, determine how many times it occurs in the `strings` list,
    and return a list of these counts in the same order as the queries.

    Parameters
    ----------
    strings : list of str
        The list of strings to search through. Each string has a length between 1 and 20.
    queries : list of str
        The list of query strings to count. Each query has a length between 1 and 20.

    Returns
    -------
    list of int
        A list of integers where the i-th element is the number of times
        queries[i] occurs in the `strings` list.

    Constraints
    -----------
    - 1 <= len(strings) <= 1000
    - 1 <= len(queries) <= 1000
    - 1 <= len(strings[i]), len(queries[i]) <= 20

    Example
    -------
    >>> matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'])
    [2, 1, 0]
    # 'ab' occurs twice, 'abc' occurs once, 'bc' occurs zero times.
    """
    stuff = []

    for q in queries:
        q_count = 0 
        for s in strings:
            if q == s:
                q_count += 1
            else:
                continue
        stuff.append(q_count)
    
    return stuff

print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))