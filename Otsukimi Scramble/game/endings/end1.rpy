label end1:
    
    # bad end, depend on affinity, slightly different different
    if affinity > 0:
        call end1_better
    else:
        call end1_bad
    #show ending text
    return

label end1_bad:
    return

label end1_better:
    return