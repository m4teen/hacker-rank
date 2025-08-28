def sockMerchant(n, ar):
    grand_total = 0
    # need to loop over unique items
    unique_els = list(set(ar))
            
    for i in range(len(unique_els)):
        y = ar.count(unique_els[i])
            
        ind_pairs_total = y//2
        grand_total += ind_pairs_total
    
    return grand_total