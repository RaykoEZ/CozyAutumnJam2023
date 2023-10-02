# TODO: Flesh out dialogue in chapter 3
label chapter3:
    scene sky evening:
        zoom 3.0
    with fade
    k "Well, what's our next move?"
    call chapter3_ChooseLocation from _call_chapter3_ChooseLocation
    # go to shrine dwelling
    return

menu chapter3_ChooseLocation:
    "Where shall we go?"
    "Go to the convenient store":
        p "Let's get some quick grub before anything."
        k "Yes...Oh! I mean sure, let's go, I haven't eaten anything since I left home!"
        scene black with fade
        call chapter3_shop from _call_chapter3_shop
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
        scene black with fade
        call chapter3_room from _call_chapter3_room
        return
# We eat some food, talk to clerk, get out, get rained on, snooze under shelter
label chapter3_shop:
    
    $ affinity -= 1
    $ affinity += 1
    return
# We snooze on bed, kaguya annoys us, do some research on PC
label chapter3_room:
    # clue triggers
    $ identityKnown = True
    $ talesOfSacrifce = True
    return