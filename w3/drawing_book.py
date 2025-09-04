def pageCount(n, p):
    """
    Determine the minimum number of page turns required to reach a target page
    in a book. You may open the book from the front or back. When you open, you
    turn two pages at a time (one left, one right).

    Parameters:
        n (int): Total number of pages in the book.
        p (int): Target page number to reach.

    Returns:
        int: Minimum number of page turns needed.

    Behaviour:
        - When starting from the front, you begin before page 1.
        - When starting from the back, if n is odd you begin after page n; if even, after page n+1.
        - Each turn flips two pages.

    Example:
        >>> pageCount(6, 2)
        1
        (From front: turn once to reach pages [1,2]; page 2 is visible.)

        >>> pageCount(5, 4)
        0
        (From back: book has pages [4,5] at last spread; target page is visible immediately.)

        >>> pageCount(5, 4)
        0
    """
    ...
    x = p / n
    minp = None
    if p == n or x == 1:
        minp = 0 
    else:
        if x <= 1/2:
            minp = p // 2
        else:
            if n % 2 == 0:
                minp = (n-p + 1) // 2
                
            else:
                minp = (n-p)//2

    return minp