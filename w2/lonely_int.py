def lonelyinteger(a):
    """
    Identify the single integer that does not repeat in a list.

    Each element in the given list `a` appears exactly twice,
    except for one solitary integer. That integer is the “lonely” one.

    Parameters:
        a (list of int): A list of integers of odd length. Every value
            appears exactly twice, except one unique integer.

    Returns:
        int: The integer that occurs only once in the list `a`.

    Example:
        a = [1, 1, 2, 2, 3]
        returns 3
    """
    for i in range(len(a)):
        if all(a[i] - x != 0 for x in a[:i]+ a[i+1:]):
            lonely = a[i] 
        else:
            continue
    return lonely

