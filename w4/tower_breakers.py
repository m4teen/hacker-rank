def towerBreakers(n: int, m: int) -> int:
    """
    Determine the winner of the Tower Breakers game.

    Two players play alternately. There are n identical towers, each of height m.
    A move consists of selecting a tower of height h > 1 and reducing it to some
    height y such that 1 ≤ y < h and y divides h. If a player cannot move, he loses.

    Rules of outcome:
        - If m == 1, Player 1 has no move and loses. Return 2.
        - If n is even, Player 2 can mirror Player 1's moves and wins. Return 2.
        - If n is odd and m > 1, Player 1 breaks symmetry and wins. Return 1.

    Args:
        n (int): Number of towers.
        m (int): Initial height of each tower.

    Returns:
        int: 1 if Player 1 wins under optimal play, 2 if Player 2 wins.
    """
    if m == 1:
        return 2
    elif n % 2 ==0:
        return 2
    elif n % 2 != 0:
        return 1
