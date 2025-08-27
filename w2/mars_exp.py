def marsExploration(s):
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
