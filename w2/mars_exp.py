def mars_exploration(s):
    """
    Given a received signal string s, composed of repeated 'SOS' transmissions of length multiple of 3,
    count and return the number of characters that differ from the expected 'SOS' pattern.

    Parameters:
        s (str): The received message, uppercase letters only, length divisible by 3.

    Returns:
        int: The count of characters altered by interference.

    Example:
        >>> mars_exploration("SOSSPSSQSSOR")
        3
        >>> mars_exploration("SOSSOT")
        1
        >>> mars_exploration("SOSSOSSOS")
        0
    """
    s = list(s) 
    og = ['S','O','S']
    err = 0 
    for i in range(0,len(s)-1, 3):
        if s[i:i+3] == og:
            continue
        else:
            p = [s[j] for j in [i,i+1,i+2] if s[j] != og[j-i]]
            err += len(p)
    return err 
