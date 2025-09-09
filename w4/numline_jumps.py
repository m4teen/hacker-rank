def kangaroo(x1, v1, x2, v2):
    """
    Determine whether two kangaroos will ever land simultaneously on the same number-line point.

    Given:
      x1, v1: starting position and jump distance of kangaroo 1.
      x2, v2: starting position and jump distance of kangaroo 2.
    Both species jump in the positive direction.

    Returns:
      'YES' — if there exists an integer t ≥ 0 such that
        x1 + t·v1 == x2 + t·v2,
      'NO' — otherwise.
    """
    if v1==v2:
        if x1==x2:
            return 'YES'
        else:
            return 'NO'
    elif (x1 - x2) % (v1-v2) == 0 and (x1-x2)//(v2-v1) >= 0:
        return 'YES'
    else:
        return 'NO'
