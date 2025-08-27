def birthday(s, d, m):
    candidates = 0
    for i in range(len(s)-m+1):
        x = s[i:i+m]
        
        if sum(x) == d:
            candidates += 1
        else:
            continue
    return candidates