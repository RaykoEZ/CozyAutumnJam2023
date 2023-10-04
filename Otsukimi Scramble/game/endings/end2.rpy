label end2:
    "end 2"
    # do ending stuff here
    if affinity > 0:
        call end2x from _call_end2x

    call ThanksForPlaying from _call_ThanksForPlaying_1
    return

# secret route unlock scene
label end2x:
    call ThanksForPlaying from _call_ThanksForPlaying_2

    # extra ending
    return