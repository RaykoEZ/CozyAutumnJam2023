# TODO: Flesh out dialogue in chapter 2
label chapter2:
    scene black with dissolve
    "We ran as fast as we could."
    scene shrine hill evening:
        zoom 3.0
    with dissolve
    "Once we safely reached the foot of the stairs leading to H. Shrine, I breath a sign of relief."
    p "We should be safe around here."
    "The Moon Festival takes place here tonight, so we should be able to blend in with the crowds."
    show kag norm
    """I was responsible for the silver-grass procurement. 

    Thanks to this Kaguya girl's meteoric entrance, pulverizing most of the supplies planned for tonight. 

    I'll need to report the damages to the organizers.
    """
    
    k "Say, I still don't know your name."
    """She's still trying to drag me into her mess, this cannot be good.
    
    The commotion at the field would have attracted the police by now.
    
    I would be in deep trouble if I were to associate with the perpetrator of that massive hole in the ground.
    """
    p "Now if you'll excuse me, I need to go."
    show kag surprise:
        zoom 0.75
    with vpunch 
    k "Hey!"
    # surprise
    show kag angry with hpunch
    p "Aargh!"
    "My neck jerks back as she grips onto the back of my shirt collar and pulls me back."
    "Looks like I won't be getting away easily."
    call decideToHelp
    # return to main
    return
label decideToHelp:
    menu: 
        "What should I do?"
        "Fine.":
            call chapter2_1
        # refuse to help
        "No, this is too much for me.":           
            # sad/frown
            show kag sad
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
    k "my mission - inquisitor"
    return

label chapter2_2:
    
    "No help"
    $ refuseToHelp = True;
    return