define inquisitor = Character("The Inquisitor")
define clerk = Character("Store Clerk")
# TODO: Flesh out dialogue in chapter 4
label chapter4_Shrine:  
    scene shrine night  
    "We arrive at the shrine and wait"
    "Encount here"
    jump inquisitorEncounter

label chapter4_Park:
    scene field night
    "We reach the park"
    "Sees a figure near the crater" 
    $ identityKnown = True
    jump inquisitorEncounter

label inquisitorEncounter:
    scene shrine night
    #TODO: Flesh out decisions on encounter with Inquisitor
    call questioning1
    inquisitor "You better know what you are talking about. I don't take kindly to slanders."
    call questioning2
    # if player presents silvergrass to the inquisitor (trap), trigger a sacrifice route
    if giveGrass:
        jump inquisitorSacrifice
    # good end
    if inquisitorScore > 1:
        jump end2
    else:
        jump inquisitorReject

menu questioning1:
    "What brings you two here?"
    "To meet you, Mister Inquisitor.": 
        $ inquisitorScore += 1
        return
    "We heard about a suspicious individual...":
        $ inquisitorScore -= 1
        return 
    "Just Sightseeing.":
        return
# if you give grass, inquisitor will scarifice himself

menu questioning2:
    "What should I do next?"
    "Let Kaguya handle this": 
        return
    "Reveal the Inquisitor's motives":
        return 
    # activate trap if player brought grass to the showdown
    "Present the silvergrass" if hasGrass:
        $ giveGrass = True
        return

# When you fail the questioning
label inquisitorReject:
    jump end1
# Trigger Trap Bad Ending
label inquisitorSacrifice:
    jump end1

# Head to Lost
label chapter4_Store:
    scene shop with dissolve
    show kag awkward
    "We arrive at the convenience store."
    k "I don't see anything suspicious here."
    p "Let's not be too impatient."
    "I enter the store, Kaguya stays outside to look out for the Inquisitor."
    "Come to think of it, I'm getting a bit peckish, I hope they haven't thrown away the sandwiches yet."
    scene sky night with dissolve
    "Hours went by, we did not see anyone of interest."
    show kag awkward
    clerk "Oh, you two still here?"
    "The store clerk came out the back door, probably coming off his shift."
    p "Yeah, our friend is running a bit late."
    clerk "Ah, it's getting a bit chilly outside, you're welcome to wait in our seating area."
    p "Thanks for the offer, we'll go in a minute."
    scene black with dissolve
    "In the end, no one, except a few night owls, came into the store."
    jump chapter4_Lost
# Head to Lost
label chapter4_Room:
    scene room with dissolve
    """It's nice to take a break from the ordeals awaiting us.
    
    My eyelids feel heavy as I dive into bed.
    
    Everything about today was exhausting.

    School assignments, work, a crash-landed alien girl, destroying my fruits of labor...
    
    and dragging me into her mess... 
    
    I need a break from this..."""
    show kag surprise
    p "zzz..."
    #zoom in
    show kag awkward
    k "Hey, can we save bed time for a bit later? We have a rabbit to catch!"
    #zoom in more
    show kag shake
    "I didn't take long to fall asleep, despite the incessant shaking from an agitated girl."
    #zoom in more
    show kag shake
    p "zzz..."
    jump chapter4_Lost
# Got to ending 1
label chapter4_Lost:
    scene black with dissolve
    show kag shadow
    """As night is approaching its end, Kaguya moves out on her own, desperately searching for any traces of the Moon Rabbit.
    
    Afterall, she stands to lose everything if she fails this.

    It's too late, we don't have time to check every place in town.
    
    In the end, we failed to find the Inquisitor."""
    jump end1


