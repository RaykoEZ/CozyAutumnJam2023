label chapter2:
    scene black with dissolve
    "We ran as fast as we could."
    scene shrine hill evening:
        zoom 3.0
    with dissolve
    """Once we safely reached the foot of the stairs leading to T. Shrine, I breath a sign of relief.
    
    The soft rustling of fallen leaves and swaying branches bring me with a familiar feeling of serenity."""
    
    p "We should be safe around here."
    "The Moon Festival takes place here tonight, so we should be able to blend in with the preparation staff."
    show kag norm   
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
    call decideToHelp
    # return to main
    return
label decideToHelp:
    menu: 
        "Looks like I won't be getting away easily."
        "Fine.":
            call chapter2_1
        # refuse to help
        "No, this is too much for me.":           
            # sad/frown
            show kag sad
            menu:
                "..."
                "Fine I'll help":
                    call chapter2_1
                "No":
                    call chapter2_2           
    return

label chapter2_1:
    p "Fine, I'll help, but don't do anything reckless, the police are probably on edge after what you did."
    p "My name is [povName]."
    # atl animation for excitement
    show kag shake with vpunch
    k "Yes Mr. [povName]! Thank you!"
    "Kaguya rigorously shakes my hands in excitement."
    p "[povName] is fine, now stop tearing my limbs apart!"
    show kag happy
    k "Ah Sorry about that~"
    "She sticks her tongue out mischievously."
    p "Hmph, so, what help do you need?"
    show kag norm
    k "I am trying to find someone."
    show kag awkward
    p "Any ideas of what this person might look like?"

    show kag shake with hpunch
    k """He's a forceful-yet-charming boss man. We used to call him the Inquisitor!

    He might look like one of those muscular high schoolers with mysterious superpowers! 
    """
    p "Uh-I'm afraid I've no clue where to start."
    # Option on what to do next
    show kag awkward
    "Silence ensues as Kaguya leans against the railings by the stone steps, deep in thought."
    k "Hmm..."
    show kag angry
    k "..."
    menu:
        "What we do next?"
        "Go to the shrine":
            """I need to report our silver-grass situation to the organizers at the shrine anyway.

            There mght be some clues to the identity of this Inquisitor."""
            p "We can ask the shrine workers. It's better than standing around here."
            show kag norm
            "She snaps out of her frustration and nods eagerly."
            k "Let's! You lead the way!"
            call chapter2_shrine
        "Ask Kaguya about the Inquisitor":
            show kag norm
            p ""
            
        "Ask more about Kaguya":
            show kag norm
            p ""
            
    #TODO: Finish Chapter 2_1 dialogue here
    return

define shrineStaff = Character("Shrine Staff")
define shrineElder = Character("Shrine Elder")
# go to shrine to ask for info
label chapter2_shrine:
    scene shrine hill evening:
        zoom 3.0
    with fade
    """
    Lucky for her, I'm an acquaintance of the workers in this shrine and a regular at the shrine. 
    
    A few of them should be staying at the dwelling behind of the sanctuary.
    """
    scene shrine evening:
        zoom 3.0
    with fade
    "As we arrive at the entrance of the shrine, we are greeted by a shrine steward." 
    shrineStaff "[povName]? Hey [povName]!"
    shrineStaff "Good to see you here, how's tonight's harvest?"
    p "Well, you see..."
    shrineElder ""
    # clue triggers
    $ identityKnown = True
    $ witnessedInquisitor = True
    $ talesOfSacrifce = True

    return
#refuse to help kaguya
label chapter2_2:
    p "I am sorry but I cannot help you any further."
    show kag surprise
    k "..."
    p "The shrine workers can help you more than I can."
    show kag norm
    k "Okay, I understand."
    show kag awkward
    k "I'm sorry we have to meet in such a way."    
    $ refuseToHelp = True
    hide kag with fade
    scene clear sky with dissolve
    "Kagari and I parted ways."
    return