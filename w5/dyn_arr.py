def dynamicArray(n, queries):
    """
    Processes a series of dynamic array queries.

    Args:
        n (int): Number of empty sequences to initialise.
        queries (list of list of int): Each query is of the form [t, x, y], where:
            - If t == 1: Append y to the sequence at index ((x XOR lastAnswer) % n).
            - If t == 2: Find the element at index (y % len(sequence)) in that sequence,
              set lastAnswer to that value, and record it.

    Returns:
        list of int: The list of all values of lastAnswer produced by type 2 queries.
    """
    arr = [[] for i in range(n)]
    lastAnswer = 0 
    answers = []
    for query in queries:
        if query[0] == 1:
            x = query[1]
            y = query[2]
            idx = (x ^ lastAnswer) % n 
            arr[idx].append(y)
        elif query[0] == 2:
            x = query[1]
            y = query[2]
            idx = (x ^ lastAnswer) % n
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)
        
    return answers