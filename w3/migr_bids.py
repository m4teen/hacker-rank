def migratoryBirds(arr):
    """
    Identify the most frequently sighted bird type, choosing the smallest ID in case of a tie.

    Given a list of integers representing bird type sightings (IDs all in range 1–5),
    determine which type appears most often and return its ID. If multiple types share the
    highest frequency, return the lowest ID among them.

    Parameters:
        arr (list[int]): List of bird type IDs sighted.

    Returns:
        int: The ID of the most frequently sighted bird, lowest ID if tie.

    Example:
        >>> migratoryBirds([1, 1, 2, 2, 3])
        1
        (Types 1 and 2 appear twice; return the lower ID: 1.)

        >>> migratoryBirds([3, 3, 2, 1, 2, 1])
        1
        (Types 1, 2 and 3 each appear twice; lowest ID is 1.)
    """
    arr_uniq = sorted(list(set(arr)))
    id_counts = {}
    for bird_id in arr_uniq:
        x = arr.count(bird_id)
        id_counts[bird_id] = x
    
    max_id = max(id_counts.values())
    ke = [k for k,v in id_counts.items() if v == max_id]
    tr_id = min(ke)
    
    return tr_id