label chapter3:
    "As we sit in front of the "
    "Where should we start?"
    call chapter3_ChooseAction
    k "Sure, let's go."
    call chapter3_ChooseLocation
    # go to shrine dwelling
    "ask shrine workers"
    "ask about what happened at the park"
    return
# talk about the events with kaguya
menu chapter3_ChooseAction:
    "What now?"
    "Let's talk":
        call chapter3_talkExtended
        return
    "Let's go somewhere and ask around":
        p "No point twiddling our thumbs here, let's gather some clues elsewhere."
        return

default chapter3_locationSet = set()
menu chapter3_ChooseLocation:
    set chapter3_locationSet
    "Where shall we go?"
    "Ask around the shrine":
        call chapter3_shrine
        return
    "Go to the convenient store":
        call chapter3_shop
        return
    "Do some research at my dorm":
        call chapter3_room
        return
    "I think we have enough information":
        return

# optional dialogue path 
label chapter3_talkExtended:
    p "To start off, what was that landing?"
    k "A slight miscalculation."
    "..."
    # trap trigger
    $ needSilverGrass = True
    return
# go to shrine to ask for info
label chapter3_shrine:
    """Lucky for her, I'm an acquaintance of the workers in this shrine and a regular at the shrine. 
    
    A few of them should be staying at the dwelling behind of the sanctuary.   

    I'll need to report the damages on the silvergrass as soon as possible
    
    Maybe we can find some clues about this Moon Rabbit.""" 
    # clue triggers
    $ identityKnown = True
    $ witnessedInquisitor = True
    $ talesOfSacrifce = True

    return

label chapter3_shop:  
    # clue triggers
    $ witnessedInquisitor = True
    $ needSilverGrass = True
    return

label chapter3_room:
    # clue triggers
    $ witnessedInquisitor = True
    $ talesOfSacrifce = True
    return