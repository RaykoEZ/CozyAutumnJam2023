label chapter2:
    scene black with dissolve
    "We ran as fast as we could"
    scene shrine hill evening with dissolve
    show kag norm
    p "okay, we should be okay"
    p "And I shall take my leave-"
    # surprise
    show kag norm
    k "Hey, you promised"
    p "..."
    call decideToHelp
    # return to main
    return
label decideToHelp:
    menu: 
        "Damn it, I wanna go home"
        "Okay, fine":
            call chapter2_1
        # refuse to help
        "No, this is all too much":           
            # sad/frown
            show kag norm
            k "..."
            "pleading eyes"
            menu:
                "..."
                "Fine I'll help":
                    call chapter2_1
                "No":
                    call chapter2_2

            
    return

label chapter2_1:
    k "ty"
    p "tell me about yourself"
    k "about yourself"
    p "tell me what your mission is"
    k "my mission"
    return

label chapter2_2:
    

    $ refuseToHelp = True;
    return