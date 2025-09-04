def maximumPerimeterTriangle(sticks):
    """
    From a list of stick lengths, select three sticks that form a non-degenerate triangle
    with the maximum possible perimeter. Return the side lengths in non-decreasing order.

    If multiple valid triangles share the maximum perimeter:
      1. Choose the one with the longest maximum side.
      2. If still tied, choose the one with the longest minimum side.
      3. If still tied, any one is acceptable.

    If no valid triangle can be formed, return [-1].

    Parameters:
        sticks (list[int]): Available stick lengths.

    Returns:
        list[int]: Three side lengths in non-decreasing order if a triangle exists;
                   otherwise [-1].

    Example:
        >>> maximumPerimeterTriangle([1, 1, 1, 3, 3])
        [1, 3, 3]
        (Triangle options include [1, 1, 1] with perimeter 3,
         and [1, 3, 3] with perimeter 7; choose the latter.)

        >>> maximumPerimeterTriangle([1, 2, 3])
        [-1]
        (These cannot form a valid triangle.)
    """    
    candidates = []
    for i in range(len(sticks)):
        for j in range(i+1,len(sticks)):
            for k in range(j+1,len(sticks)):
                if sticks[i] + sticks[j] > sticks[k] and sticks[i] + sticks[k] > sticks[j] and sticks[k] + sticks[j] > sticks[i]:
                    d = sorted([sticks[i],sticks[j],sticks[k]])
                    d = tuple(d)
                    candidates.append(d)  
                else: 
                    continue
    if len(candidates) != 0:
        perims = []
        mxlist = []
        mnlist = []
        for i in range(len(candidates)):
            perim = sum(candidates[i])
            mn = min(candidates[i])
            mx = max(candidates[i])
            
            perims.append(perim)
            mxlist.append(mx)
            mnlist.append(mn)
            
        valid_val = max(perims)
        valids = [i for i in range(len(perims)) if perims[i] == valid_val]
        
        mxcrit_val = max(mxlist)
        mncrit_val= max(mnlist)
        
        critmx = [i for i in range(len(mxlist)) if mxlist[i] == mxcrit_val]
        critmin = [i for i in range(len(mnlist)) if mnlist[i] == mncrit_val]
        
        chosen_i = [val for val in valids if val in critmx and val in critmin ]
        
        m = chosen_i[0]
        ans = candidates[m]
    
    else:
        ans = [-1]
        
    return ans
