def pangrams(s: str) -> str:
    """
    Assess whether a given sentence is a pangram—a sentence containing
    every letter of the English alphabet at least once, ignoring case.

    Parameters:
        s (str): The sentence to evaluate; may contain spaces, upper- and lower-case letters.

    Returns:
        str: 'pangram' if all letters a–z appear at least once, otherwise 'not pangram'.

    Example:
        >>> pangrams("We promptly judged antique ivory buckles for the next prize")
        'pangram'
        >>> pangrams("We promptly judged antique ivory buckles for the prize")
        'not pangram'
    """
    s = s.lower()
    s = list(s)
    alphs = [chr(i) for i in range(97,123)]
    x=0
    for i in range(len(alphs)):
        if alphs[i] in s:
            x +=1
        else:
            continue
    if x == 26:
        y = 'pangram'
    else:
        y = 'not pangram'
    return y