def caesarCipher(s, k):
    """
    Encrypt the input string using a Caesar cipher.

    Each alphabetic character in the string s (cleartext) is shifted forward
    by k positions in the alphabet. Letters wrap around (‘z’ to ‘a’, ‘Z’ to ‘A’) 
    when the shift exceeds the end of the alphabet. Non-alphabetic characters
    remain unchanged.

    Parameters
    ----------
    s : str
        The string to encrypt; contains printable ASCII characters without spaces.
    k : int
        The rotation factor, the number of positions to shift each letter.

    Returns
    -------
    str
        The encrypted string (ciphertext).

    Behaviour
    ---------
    - Compute k mod 26 to confine shift to a single alphabet cycle.
    - Letters in 'a'–'z' and 'A'–'Z' are rotated accordingly; case preserved.
    - Characters outside these ranges (e.g. '-', digits, punctuation) remain as-is.

    Input Format (HackerRank specification)
    ----------------------------------------
    First line: integer representing the length of the cleartext string (not used in code).
    Second line: the string s to be encrypted.
    Third line: integer k denoting the rotation factor.

    Example
    -------
    Given:
        s = "middle-Outz"
        k = 2

    The function returns: "okffng-Qwvb"
      Explanation:
        m -> o, i -> k, d -> f, d -> f, l -> n, e -> g
        '-' remains '-'
        O -> Q, u -> w, t -> v, z -> b

    Complexity
    ----------
    Time Complexity: O(n), where n is the length of s.
    Space Complexity: O(n), for constructing the output string.
    """
    s = list(s)
    s_c = s[::]
    
    for i in range(len(s)):
        if ord(s[i]) in range(97,123):
             s[i] = chr((ord(s_c[i])+k-97) % 26 +97) 
        elif ord(s[i]) in range(65,91):
            s[i] = chr((ord(s_c[i])+k-65) % 26 +65) 
    
    s = ''.join(s)
    
    return s
    