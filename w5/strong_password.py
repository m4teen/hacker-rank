def minimumNumber(n, password):
    """
    Determine the minimum number of characters to add to make a password strong.

    A strong password must satisfy all of these criteria:
      1. Length at least 6 characters.
      2. Contains at least one digit. 
      3. Contains at least one lowercase English character.
      4. Contains at least one uppercase English character.
      5. Contains at least one special character from: !@#$%^&*()-+ 

    Parameters:
        n (int): The current length of the password. 
        password (str): The password string to evaluate. 

    Returns:
        int: The minimum number of characters that must be added for the password to satisfy *all* strong criteria.

    Pre-conditions:
        - n equals len(password). 
        - password contains only characters from the sets: digits, lowercase, uppercase, or the special set listed above. 
    """
    l1 = ord('a')
    l2 = ord('z')
    u1 = ord('A') 
    u2 = ord('Z')
    
    digs = [str(i) for i in range(0,10)]
    lowerc = [chr(i)  for i in range(l1,l2+1)]
    upperc = [chr(i)  for i in range(u1,u2+1)]
    spec = ['!','@','#','$','%','^','&','*','(',')','-','+']
    
    password = list(password)
    pl = [p for p in password if p in lowerc]
    pu = [p for p in password if p in upperc]
    ps = [p for p in password if p in spec]
    pd = [p for p in password if p in digs]
    
    lowercdiff = 1 - len(pl)
    uppercdiff = 1 - len(pu)
    specdiff = 1 - len(ps)
    digdiff = 1 - len(pd)
    
    total = 0
    if lowercdiff <= 0 and uppercdiff <= 0 and specdiff <=0 and digdiff <= 0 and len(password) >= 6:
        return total
    else:
        if lowercdiff > 0:
            total += lowercdiff
        if uppercdiff > 0: 
            total += uppercdiff
        if specdiff > 0:
            total += specdiff
        if digdiff > 0:
            total += digdiff 
        if total + len(password) <6:
            total += 6 - (total + len(password))
        
        return total 
        
     