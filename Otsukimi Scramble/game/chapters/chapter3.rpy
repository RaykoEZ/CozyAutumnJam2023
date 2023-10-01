# TODO: Flesh out dialogue in chapter 3
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
    "Go to the convenient store":
        call chapter3_shop
        return
    "Search for clues on the internet":
        p """Let's go to my place, 
        
        there should be records on the internet if your friend entered the Earth in a similar manner.
        """
        show kag surprise
        k "Inta-net?"
        "Ignoring her questioning gaze, I gesture her to follow my lead."
        "A break from being outside all day, the timing cannot be better!"
        p "Let's go back to my place, we have little time to waste!"
        k "O-okay!"
        call chapter3_room
        return

# optional dialogue path 
label chapter3_talkExtended:
    p "To start off, what was that landing?"
    k "A slight miscalculation."
    "..."
    # trap trigger
    $ needSilverGrass = True
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