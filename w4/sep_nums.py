def separateNumbers(s):
    """
    Determine if the numeric string s qualifies as 'beautiful'.

    A string is 'beautiful' if it can be split into a sequence of at least two
    positive integers (no leading zeros), each exactly one greater than its predecessor.
    The order must match the string's original order, without rearrangement.

    Prints:
        - If beautiful: "YES x", where x is the smallest valid first number.
        - Otherwise: "NO".

    Parameters:
        s (str): A numeric string to evaluate.

    Behaviour:
    1. For each possible starting number length from 1 to len(s)//2:
         a. Extract the first number candidate from the initial segment of s.
         b. Reject it immediately if it begins with '0' (leading zeros forbidden).
         c. Build the anticipated complete sequence by successively appending
            incremented values until the constructed string equals or exceeds len(s).
         d. If constructed string equals s exactly, output "YES {first number}" and halt.
    2. If no candidate succeeds, output "NO".

    No return value (side-effect: prints result).
    """
    candidates =[]
    for i in range(1,len(s)//2+1):
        seq = s[0:i]
        if seq[0] == '0':
            continue
        x = seq
        n = int(seq)
        while len(x) < len(s):
            n += 1
            x += str(n)
                 
        if x == s:
            candidates.append(seq)
        else:
            continue
    if len(candidates) != 0:
        y = min(candidates)
        print('YES', y)
    else:
        print('NO')
    