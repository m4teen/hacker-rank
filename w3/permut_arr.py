def twoArrays(k, A, B):
    A = sorted(A)
    B = sorted(B,reverse =True)
    h = 'YES'
    for i in range(len(A)):
        x = A[i]+B[i]
        
        if x >= k:
            continue 
        else:  
            h = 'NO'
            break
    
    
    return h